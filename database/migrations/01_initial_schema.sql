-- Phase 2: Database Schema
-- Run this in PostgreSQL connected to the target database.

-- Enable PostGIS and UUID extensions
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. sources
CREATE TABLE IF NOT EXISTS sources (
    source_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    base_url VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. raw_listings
CREATE TABLE IF NOT EXISTS raw_listings (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    source VARCHAR(255) NOT NULL,
    source_listing_id VARCHAR(255),
    url TEXT UNIQUE,
    title_raw TEXT,
    description_raw TEXT,
    price_raw VARCHAR(255),
    area_raw VARCHAR(255),
    address_raw TEXT,
    district_raw VARCHAR(255),
    ward_raw VARCHAR(255),
    commune_raw VARCHAR(255),
    city_raw VARCHAR(255),
    project_raw VARCHAR(255),
    urban_area_raw VARCHAR(255),
    building_raw VARCHAR(255),
    block_raw VARCHAR(255),
    latitude_raw VARCHAR(255),
    longitude_raw VARCHAR(255),
    published_at_raw VARCHAR(255),
    updated_at_raw VARCHAR(255),
    collected_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    raw_content JSONB
);

CREATE INDEX idx_raw_listings_source_id ON raw_listings(source, source_listing_id);
CREATE INDEX idx_raw_listings_collected_at ON raw_listings(collected_at);

-- 3. properties
CREATE TABLE IF NOT EXISTS properties (
    property_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    property_type VARCHAR(100),
    property_subtype VARCHAR(100),
    transaction_type VARCHAR(50),
    price_vnd NUMERIC,
    price_per_m2 NUMERIC,
    area_m2 NUMERIC CHECK (area_m2 > 0 OR area_m2 IS NULL),
    city VARCHAR(100),
    old_district VARCHAR(100),
    old_ward VARCHAR(100),
    new_ward VARCHAR(100),
    street VARCHAR(255),
    address TEXT,
    normalized_address TEXT,
    project VARCHAR(255),
    urban_area VARCHAR(255),
    building VARCHAR(255),
    block VARCHAR(100),
    floor INT,
    total_floors INT,
    bedrooms INT,
    bathrooms INT,
    frontage_m NUMERIC,
    depth_m NUMERIC,
    alley_width_m NUMERIC,
    direction VARCHAR(50),
    balcony_direction VARCHAR(50),
    furniture VARCHAR(100),
    view VARCHAR(100),
    parking BOOLEAN,
    legal_status VARCHAR(100),
    planning_status VARCHAR(100),
    latitude FLOAT,
    longitude FLOAT,
    location_precision VARCHAR(50),
    data_quality INT CHECK (data_quality BETWEEN 0 AND 100),
    published_at TIMESTAMP WITH TIME ZONE,
    collected_at TIMESTAMP WITH TIME ZONE,
    last_seen_at TIMESTAMP WITH TIME ZONE,
    geom geometry(Point, 4326)
);

CREATE INDEX idx_properties_type ON properties(property_type);
CREATE INDEX idx_properties_new_ward ON properties(new_ward);
CREATE INDEX idx_properties_geom ON properties USING GIST (geom);

-- 4. property_snapshots
CREATE TABLE IF NOT EXISTS property_snapshots (
    snapshot_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    property_id UUID REFERENCES properties(property_id) ON DELETE CASCADE,
    snapshot_date DATE NOT NULL,
    area_m2 NUMERIC,
    price_vnd NUMERIC,
    price_per_m2 NUMERIC,
    property_type VARCHAR(100),
    property_subtype VARCHAR(100),
    address TEXT,
    new_ward VARCHAR(100),
    project VARCHAR(255),
    building VARCHAR(255),
    bedrooms INT,
    bathrooms INT,
    floor INT,
    total_floors INT,
    legal_status VARCHAR(100),
    source VARCHAR(255),
    listing_id VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_snapshots_property_id ON property_snapshots(property_id);
CREATE INDEX idx_snapshots_date ON property_snapshots(snapshot_date);

-- 5. property_events
CREATE TABLE IF NOT EXISTS property_events (
    event_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    event_type VARCHAR(100) NOT NULL, -- split, merge, rebuild, etc.
    source_property_id UUID REFERENCES properties(property_id),
    target_property_id UUID REFERENCES properties(property_id),
    event_date DATE,
    evidence TEXT,
    confidence VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_events_source ON property_events(source_property_id);
CREATE INDEX idx_events_target ON property_events(target_property_id);

-- 6. admin_areas
CREATE TABLE IF NOT EXISTS admin_areas (
    admin_area_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    normalized_name VARCHAR(255) NOT NULL,
    type VARCHAR(50) NOT NULL, -- city, district, ward, commune
    parent_id INT REFERENCES admin_areas(admin_area_id),
    valid_from DATE,
    valid_to DATE,
    geom geometry(MultiPolygon, 4326)
);

CREATE INDEX idx_admin_areas_geom ON admin_areas USING GIST (geom);
CREATE INDEX idx_admin_areas_normalized_name ON admin_areas(normalized_name);

-- 7. data_quality_checks
CREATE TABLE IF NOT EXISTS data_quality_checks (
    check_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    entity_id UUID NOT NULL, -- references property_id or snapshot_id
    entity_type VARCHAR(50) NOT NULL, -- 'property' or 'snapshot'
    check_name VARCHAR(100) NOT NULL,
    check_result VARCHAR(50), -- 'passed', 'failed', 'warning'
    score INT,
    details JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_quality_entity ON data_quality_checks(entity_id, entity_type);

-- 8. ml_property_dataset
CREATE TABLE IF NOT EXISTS ml_property_dataset (
    ml_record_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    property_id UUID UNIQUE REFERENCES properties(property_id),
    snapshot_id UUID REFERENCES property_snapshots(snapshot_id),
    property_type VARCHAR(100),
    property_subtype VARCHAR(100),
    price_vnd NUMERIC,
    price_per_m2 NUMERIC,
    area_m2 NUMERIC,
    bedrooms INT,
    bathrooms INT,
    floor INT,
    total_floors INT,
    frontage_m NUMERIC,
    alley_width_m NUMERIC,
    direction VARCHAR(50),
    project VARCHAR(255),
    building VARCHAR(255),
    new_ward VARCHAR(100),
    latitude FLOAT,
    longitude FLOAT,
    legal_status VARCHAR(100),
    planning_status VARCHAR(100),
    snapshot_quality_score INT,
    geom geometry(Point, 4326),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_ml_geom ON ml_property_dataset USING GIST (geom);
CREATE INDEX idx_ml_ward ON ml_property_dataset(new_ward);
CREATE INDEX idx_ml_type ON ml_property_dataset(property_type);
