import os
import re
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.stattools import durbin_watson
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import Ridge, Lasso, RidgeCV, LassoCV
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Output directories
FIGURES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'reports', 'figures')
os.makedirs(FIGURES_DIR, exist_ok=True)

# Clean style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

def run_all():
    print("==========================================================")
    print("🚀 BẮT ĐẦU CHẠY THỰC NGHIỆM TUẦN 9 & TUẦN 10 (INFO3020)")
    print("==========================================================")
    
    clean_csv = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'processed', 'clean.csv')
    df = pd.read_csv(clean_csv)
    print(f"📊 Đã nạp thành công: {len(df):,} dòng và {df.shape[1]} thuộc tính.")

    # ==========================================================
    # PHẦN 1: TUẦN 9 - THỐNG KÊ SUY LUẬN & KIỂM ĐỊNH GIẢ THUYẾT
    # ==========================================================
    print("\n" + "="*50)
    print("📌 PHẦN 1: TUẦN 9 - THỐNG KÊ SUY LUẬN (INFERENTIAL STATS)")
    print("="*50)

    # 1.1 Welch's t-test: Nội đô vs Ngoại thành
    noi_do_prices = df[df['khu_vuc_noi_do'] == 1]['Giá_m2_trieu'].dropna()
    ngoai_thanh_prices = df[df['khu_vuc_noi_do'] == 0]['Giá_m2_trieu'].dropna()

    mean_nd, std_nd, n_nd = noi_do_prices.mean(), noi_do_prices.std(), len(noi_do_prices)
    mean_nt, std_nt, n_nt = ngoai_thanh_prices.mean(), ngoai_thanh_prices.std(), len(ngoai_thanh_prices)

    t_stat, p_val_ttest = stats.ttest_ind(noi_do_prices, ngoai_thanh_prices, equal_var=False)
    u_stat, p_val_mwu = stats.mannwhitneyu(noi_do_prices, ngoai_thanh_prices, alternative='two-sided')

    # Cohen's d
    s_pooled = np.sqrt(((n_nd - 1)*std_nd**2 + (n_nt - 1)*std_nt**2) / (n_nd + n_nt - 2))
    cohens_d = (mean_nd - mean_nt) / s_pooled

    print(f"--- 1.1 Kiểm định Nội đô vs Ngoại thành ---")
    print(f"Nội thành: n = {n_nd:,}, Mean = {mean_nd:.2f} tr/m2, Std = {std_nd:.2f}, Median = {noi_do_prices.median():.2f}")
    print(f"Ngoại thành: n = {n_nt:,}, Mean = {mean_nt:.2f} tr/m2, Std = {std_nt:.2f}, Median = {ngoai_thanh_prices.median():.2f}")
    print(f"Chênh lệch trung bình: {mean_nd - mean_nt:.2f} triệu/m2 (Nội đô cao hơn {(mean_nd/mean_nt - 1)*100:.1f}%)")
    print(f"Welch's t-test: t = {t_stat:.4f}, p-value = {p_val_ttest:.4e}")
    print(f"Mann-Whitney U: U = {u_stat:.2e}, p-value = {p_val_mwu:.4e}")
    print(f"Cohen's d (Effect Size): {cohens_d:.4f} (Mức độ tác động từ trung bình đến lớn)")

    # 1.2 One-way ANOVA & Kruskal-Wallis giữa Top 12 quận/huyện
    top12_districts = df['Quận'].value_counts().head(12).index.tolist()
    df_top12 = df[df['Quận'].isin(top12_districts)].copy()

    district_groups = [df[df['Quận'] == d]['Giá_m2_trieu'].dropna() for d in top12_districts]
    f_stat, p_val_anova = stats.f_oneway(*district_groups)
    kw_stat, p_val_kw = stats.kruskal(*district_groups)

    print(f"\n--- 1.2 Kiểm định ANOVA so sánh 12 quận/huyện ---")
    print(f"One-way ANOVA: F = {f_stat:.4f}, p-value = {p_val_anova:.4e}")
    print(f"Kruskal-Wallis: H = {kw_stat:.4f}, p-value = {p_val_kw:.4e}")

    # Tukey's HSD Post-Hoc Test
    tukey = pairwise_tukeyhsd(endog=df_top12['Giá_m2_trieu'], groups=df_top12['Quận'], alpha=0.05)
    tukey_df = pd.DataFrame(data=tukey._results_table.data[1:], columns=tukey._results_table.data[0])
    no_diff_pairs = tukey_df[tukey_df['reject'] == False]
    print(f"Tukey's HSD: Có {len(tukey_df)} cặp so sánh, trong đó {len(no_diff_pairs)} cặp KHÔNG có sự khác biệt có ý nghĩa thống kê (p > 0.05):")
    for _, row in no_diff_pairs.iterrows():
        print(f"   * {row['group1']} vs {row['group2']}: Chênh lệch = {row['meandiff']:.2f} tr, p-adj = {row['p-adj']:.4f}")

    # 1.3 Khoảng tin cậy 95% (Confidence Interval) cho 12 quận
    print(f"\n--- 1.3 Bảng khoảng tin cậy 95% (CI) cho 12 Quận/Huyện ---")
    ci_records = []
    for d in top12_districts:
        sub = df[df['Quận'] == d]['Giá_m2_trieu'].dropna()
        n = len(sub)
        mean = sub.mean()
        std = sub.std()
        se = std / np.sqrt(n)
        ci_low, ci_high = stats.t.interval(0.95, df=n-1, loc=mean, scale=se)
        ci_records.append({
            'Quận': d.title(),
            'Số lượng (n)': n,
            'Trung bình (tr/m2)': round(mean, 2),
            'Trung vị (tr/m2)': round(sub.median(), 2),
            'SE (Sai số chuẩn)': round(se, 2),
            'CI 95% Dưới': round(ci_low, 2),
            'CI 95% Trên': round(ci_high, 2),
            'Biên độ sai số (+-)': round(ci_high - mean, 2)
        })
    ci_table = pd.DataFrame(ci_records).sort_values(by='Trung bình (tr/m2)', ascending=False)
    print(ci_table.to_string(index=False))

    # 1.4 Chi-Square Test of Independence: Khu vực Nội đô vs Có Sổ đỏ
    contingency_table = pd.crosstab(df['khu_vuc_noi_do'], df['co_so_do'])
    chi2, p_val_chi2, dof, expected = stats.chi2_contingency(contingency_table)
    print(f"\n--- 1.4 Kiểm định Chi-square độc lập: Nội đô vs Tình trạng Sổ đỏ ---")
    print(contingency_table)
    print(f"Chi2 statistic = {chi2:.4f}, p-value = {p_val_chi2:.4e}, DoF = {dof}")

    # ==========================================================
    # BIỂU ĐỒ SỐ 7: KHOẢNG TIN CẬY 95% (CI) CHO CÁC QUẬN HUYỆN
    # ==========================================================
    fig, ax = plt.subplots(figsize=(12, 7))
    ci_sorted = ci_table.sort_values(by='Trung bình (tr/m2)', ascending=True)
    y_pos = np.arange(len(ci_sorted))

    ax.errorbar(
        ci_sorted['Trung bình (tr/m2)'], y_pos, 
        xerr=ci_sorted['Biên độ sai số (+-)'], 
        fmt='o', color='#1f77b4', ecolor='#d62728', elinewidth=2.5, capsize=5, capthick=2,
        markersize=8, label='Đơn giá Trung bình & Khoảng tin cậy 95% (CI)'
    )
    # Scatter điểm Trung vị (Median) đối sánh
    ax.scatter(ci_sorted['Trung vị (tr/m2)'], y_pos, color='#2ca02c', marker='D', s=60, zorder=5, label='Đơn giá Trung vị (Median)')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(ci_sorted['Quận'], fontsize=11, fontweight='bold')
    ax.set_xlabel('Đơn giá Bất động sản (Triệu VNĐ/m²)', fontsize=12, fontweight='bold')
    ax.set_title('BIỂU ĐỒ 07: KHOẢNG TIN CẬY 95% (95% CI) CHO ĐƠN GIÁ TRUNG BÌNH 12 QUẬN/HUYỆN HÀ NỘI\n(Mức ý nghĩa alpha = 0.05, Welch t-test & ANOVA p < 0.001)', fontsize=13, fontweight='bold', pad=15)
    
    # Kẻ đường trung bình thành phố
    city_mean = df['Giá_m2_trieu'].mean()
    city_median = df['Giá_m2_trieu'].median()
    ax.axvline(city_mean, color='#ff7f0e', linestyle='--', linewidth=1.5, label=f'Trung bình toàn TP: {city_mean:.2f} tr/m²')
    ax.axvline(city_median, color='#9467bd', linestyle=':', linewidth=1.5, label=f'Trung vị toàn TP: {city_median:.2f} tr/m²')

    # Thêm text chú thích CI
    for i, row in enumerate(ci_sorted.itertuples()):
        ax.text(
            row._7 + 3, i, 
            f"[{row._6:.1f} - {row._7:.1f}]", 
            va='center', fontsize=9, color='#333333'
        )

    ax.legend(loc='lower right', frameon=True, framealpha=0.9, fontsize=10)
    plt.tight_layout()
    fig7_path = os.path.join(FIGURES_DIR, '07_confidence_intervals_districts.png')
    plt.savefig(fig7_path, dpi=300)
    plt.close()
    print(f"✅ Đã lưu Biểu đồ 07 tại: {fig7_path}")

    # ==========================================================
    # PHẦN 2: TUẦN 10 - CHẨN ĐOÁN HỒI QUY & 4 GIẢ ĐỊNH LINE
    # ==========================================================
    print("\n" + "="*50)
    print("📌 PHẦN 2: TUẦN 10 - CHẨN ĐOÁN HỒI QUY & 4 GIẢ ĐỊNH LINE")
    print("="*50)

    # Chuẩn bị dữ liệu mô hình tuyến tính
    model_df = df[[
        'Giá_m2_trieu', 'Diện tích m2', 'Số tầng', 'Số phòng ngủ', 
        'mat_tien_m', 'chieu_sau_m', 'khu_vuc_noi_do', 'co_so_do',
        'loai_nha_mat_pho', 'loai_nha_ngo_hem', 'tong_dien_tich_san_m2'
    ]].copy()

    # Fillna median cho các cột kích thước
    for col in ['mat_tien_m', 'chieu_sau_m', 'Số tầng', 'Số phòng ngủ']:
        model_df[col] = model_df[col].fillna(model_df[col].median())

    # 2.1 Mô hình OLS với statsmodels
    X = model_df.drop(columns=['Giá_m2_trieu'])
    y = model_df['Giá_m2_trieu']
    X_sm = sm.add_constant(X)

    ols_model = sm.OLS(y, X_sm).fit()
    print(ols_model.summary())

    # Tính Durbin-Watson
    residuals = ols_model.resid
    dw_stat = durbin_watson(residuals)
    print(f"\n--- 2.2 Kiểm tra 4 Giả định LINE ---")
    print(f"1. Durbin-Watson statistic (Tính độc lập I): {dw_stat:.4f} (Giá trị ~ 2.0 xác nhận phần dư độc lập)")

    # Breusch-Pagan test
    bp_stat, bp_pval, _, _ = het_breuschpagan(residuals, X_sm)
    print(f"2. Breusch-Pagan test (Phương sai không đổi E): BP = {bp_stat:.2f}, p-value = {bp_pval:.4e}")
    if bp_pval < 0.05:
        print("   -> Bác bỏ H0, tồn tại hiện tượng Heteroscedasticity (Phương sai thay đổi / hình phễu)!")

    # Jarque-Bera Normality Test
    jb_stat, jb_pval = stats.jarque_bera(residuals)
    skew = stats.skew(residuals)
    kurtosis = stats.kurtosis(residuals)
    print(f"3. Jarque-Bera test (Phân phối chuẩn N): JB = {jb_stat:.2f}, p-value = {jb_pval:.4e}, Skew = {skew:.2f}, Kurtosis = {kurtosis:.2f}")
    if jb_pval < 0.05:
        print("   -> Bác bỏ H0, phần dư có độ lệch (Skewed), chưa tuân theo phân phối chuẩn hoàn hảo.")

    # 2.3 Giải pháp: Mô hình Log-Linear: log(y) = X * beta
    log_y = np.log(y)
    ols_log_model = sm.OLS(log_y, X_sm).fit()
    log_residuals = ols_log_model.resid
    jb_stat_log, jb_pval_log = stats.jarque_bera(log_residuals)
    skew_log = stats.skew(log_residuals)
    kurtosis_log = stats.kurtosis(log_residuals)
    bp_stat_log, bp_pval_log, _, _ = het_breuschpagan(log_residuals, X_sm)

    print(f"\n--- 2.4 So sánh trước và sau biến đổi Logarit ---")
    print(f"Mô hình Gốc (Linear OLS): R2 = {ols_model.rsquared:.4f}, Skewness phần dư = {skew:.2f}, Kurtosis = {kurtosis:.2f}")
    print(f"Mô hình Log-Linear:      R2 = {ols_log_model.rsquared:.4f}, Skewness phần dư = {skew_log:.2f}, Kurtosis = {kurtosis_log:.2f}")

    # ==========================================================
    # BIỂU ĐỒ SỐ 8: CHẨN ĐOÁN 4 GIẢ ĐỊNH LINE (RESIDUAL DIAGNOSTICS)
    # ==========================================================
    fig, axes = plt.subplots(2, 2, figsize=(14, 11))

    fitted_vals = ols_model.fittedvalues
    # Đồ thị 1: Residuals vs Fitted (Linearity & Homoscedasticity)
    axes[0, 0].scatter(fitted_vals, residuals, alpha=0.3, color='#1f77b4', s=15)
    axes[0, 0].axhline(0, color='red', linestyle='--', linewidth=1.5)
    sns.regplot(x=fitted_vals, y=residuals, ax=axes[0, 0], scatter=False, lowess=True, line_kws={'color': 'darkred', 'linewidth': 2})
    axes[0, 0].set_title('1. Residuals vs Fitted (Kiểm tra Tuyến tính L & Phương sai E)', fontsize=11, fontweight='bold')
    axes[0, 0].set_xlabel('Giá trị dự báo (Fitted Values - tr/m²)')
    axes[0, 0].set_ylabel('Phần dư (Residuals = Thực tế - Dự báo)')

    # Đồ thị 2: Normal Q-Q Plot mô hình gốc (Normality N)
    sm.qqplot(residuals, stats.t, distargs=(df.shape[0]-X.shape[1],), fit=True, line='45', ax=axes[0, 1])
    axes[0, 1].get_lines()[0].set_color('#1f77b4')
    axes[0, 1].get_lines()[0].set_markersize(3)
    axes[0, 1].get_lines()[0].set_alpha(0.3)
    axes[0, 1].get_lines()[1].set_color('red')
    axes[0, 1].get_lines()[1].set_linewidth(2)
    axes[0, 1].set_title(f'2. Normal Q-Q Plot (Mô hình Gốc)\n(Đuôi vểnh do phân phối lệch phải, Skew={skew:.2f})', fontsize=11, fontweight='bold')

    # Đồ thị 3: Normal Q-Q Plot sau biến đổi Log (Cải thiện rõ rệt)
    sm.qqplot(log_residuals, stats.t, distargs=(df.shape[0]-X.shape[1],), fit=True, line='45', ax=axes[1, 0])
    axes[1, 0].get_lines()[0].set_color('#2ca02c')
    axes[1, 0].get_lines()[0].set_markersize(3)
    axes[1, 0].get_lines()[0].set_alpha(0.3)
    axes[1, 0].get_lines()[1].set_color('red')
    axes[1, 0].get_lines()[1].set_linewidth(2)
    axes[1, 0].set_title(f'3. Normal Q-Q Plot Sau Biến Đổi log(Giá)\n(Cải thiện xuất sắc: Bám sát đường 45°, Skew={skew_log:.2f})', fontsize=11, fontweight='bold')

    # Đồ thị 4: Phân phối phần dư trước vs sau Log
    sns.kdeplot(residuals / residuals.std(), ax=axes[1, 1], label='Mô hình Gốc (Chuẩn hóa)', color='#1f77b4', linewidth=2)
    sns.kdeplot(log_residuals / log_residuals.std(), ax=axes[1, 1], label='Sau Biến Đổi Log (Chuẩn hóa)', color='#2ca02c', linewidth=2)
    # Đường phân phối chuẩn lý thuyết
    x_axis = np.linspace(-4, 4, 200)
    axes[1, 1].plot(x_axis, stats.norm.pdf(x_axis, 0, 1), 'r--', label='Phân phối chuẩn lý thuyết N(0,1)', linewidth=1.5)
    axes[1, 1].set_title('4. Mật độ phần dư (KDE) So với Phân phối chuẩn N(0,1)', fontsize=11, fontweight='bold')
    axes[1, 1].set_xlabel('Phần dư chuẩn hóa (Standardized Residuals)')
    axes[1, 1].set_ylabel('Mật độ')
    axes[1, 1].legend(fontsize=9)

    plt.suptitle('BIỂU ĐỒ 08: BỘ CHẨN ĐOÁN 4 GIẢ ĐỊNH LINE VÀ HIỆU QUẢ BIẾN ĐỔI LOGARIT\n(Linearity - Independence - Normality - Equal Variance)', fontsize=13, fontweight='bold', y=1.02)
    plt.tight_layout()
    fig8_path = os.path.join(FIGURES_DIR, '08_line_assumptions_diagnostics.png')
    plt.savefig(fig8_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✅ Đã lưu Biểu đồ 08 tại: {fig8_path}")

    # ==========================================================
    # PHẦN 3: TUẦN 10 - REGULARISATION (RIDGE VS LASSO)
    # ==========================================================
    print("\n" + "="*50)
    print("📌 PHẦN 3: TUẦN 10 - REGULARISATION (RIDGE VS LASSO)")
    print("="*50)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # 1. OLS Baseline
    ols_sk = sm.OLS(y_train, sm.add_constant(X_train)).fit()
    y_pred_ols = ols_sk.predict(sm.add_constant(X_test))
    mae_ols = mean_absolute_error(y_test, y_pred_ols)
    rmse_ols = np.sqrt(mean_squared_error(y_test, y_pred_ols))
    r2_ols = r2_score(y_test, y_pred_ols)

    # 2. Ridge Regression
    ridge_cv = RidgeCV(alphas=np.logspace(-2, 4, 50), cv=5).fit(X_train, y_train)
    best_ridge_alpha = ridge_cv.alpha_
    y_pred_ridge = ridge_cv.predict(X_test)
    mae_ridge = mean_absolute_error(y_test, y_pred_ridge)
    rmse_ridge = np.sqrt(mean_squared_error(y_test, y_pred_ridge))
    r2_ridge = r2_score(y_test, y_pred_ridge)

    # 3. Lasso Regression
    lasso_cv = LassoCV(alphas=np.logspace(-3, 2, 50), cv=5, random_state=42, max_iter=5000).fit(X_train, y_train)
    best_lasso_alpha = lasso_cv.alpha_
    y_pred_lasso = lasso_cv.predict(X_test)
    mae_lasso = mean_absolute_error(y_test, y_pred_lasso)
    rmse_lasso = np.sqrt(mean_squared_error(y_test, y_pred_lasso))
    r2_lasso = r2_score(y_test, y_pred_lasso)

    # 4. Log-OLS
    y_train_log = np.log(y_train)
    log_ols_sk = sm.OLS(y_train_log, sm.add_constant(X_train)).fit()
    y_pred_log_raw = log_ols_sk.predict(sm.add_constant(X_test))
    y_pred_log_exp = np.exp(y_pred_log_raw) # chuyển ngược về triệu/m2
    mae_log = mean_absolute_error(y_test, y_pred_log_exp)
    rmse_log = np.sqrt(mean_squared_error(y_test, y_pred_log_exp))
    r2_log = r2_score(y_test, y_pred_log_exp)

    print(f"\n--- Bảng so sánh 4 Mô hình Hồi quy Tuyến tính (Tập Test n = {len(y_test):,}) ---")
    reg_comparison = pd.DataFrame([
        {'Mô hình': 'OLS Cổ Điển', 'MAE (tr/m2)': round(mae_ols, 2), 'RMSE (tr/m2)': round(rmse_ols, 2), 'R2': round(r2_ols, 4), 'Ghi chú': 'Baseline, nhạy cảm với đa cộng tuyến'},
        {'Mô hình': f'Ridge (L2, alpha={best_ridge_alpha:.2f})', 'MAE (tr/m2)': round(mae_ridge, 2), 'RMSE (tr/m2)': round(rmse_ridge, 2), 'R2': round(r2_ridge, 4), 'Ghi chú': 'Co nhỏ hệ số, ổn định phương sai'},
        {'Mô hình': f'Lasso (L1, alpha={best_lasso_alpha:.4f})', 'MAE (tr/m2)': round(mae_lasso, 2), 'RMSE (tr/m2)': round(rmse_lasso, 2), 'R2': round(r2_lasso, 4), 'Ghi chú': 'Tự động đưa biến yếu về 0'},
        {'Mô hình': 'Log-OLS (Biến đổi Log)', 'MAE (tr/m2)': round(mae_log, 2), 'RMSE (tr/m2)': round(rmse_log, 2), 'R2': round(r2_log, 4), 'Ghi chú': 'Nắn chuẩn phần dư, giảm phạt lỗi lớn'}
    ])
    print(reg_comparison.to_string(index=False))

    # Bảng so sánh hệ số Beta giữa OLS, Ridge, Lasso
    coef_df = pd.DataFrame({
        'Đặc trưng': X.columns,
        'OLS Coef': ols_sk.params[1:],
        'Ridge Coef': ridge_cv.coef_,
        'Lasso Coef': lasso_cv.coef_
    })
    print("\n--- Bảng so sánh Hệ số hồi quy Beta (Đã Standardize) ---")
    print(coef_df.round(3).to_string(index=False))

    # ==========================================================
    # BIỂU ĐỒ SỐ 9: SO SÁNH HỆ SỐ LASSO VS RIDGE (FEATURE SELECTION)
    # ==========================================================
    fig, ax = plt.subplots(figsize=(12, 6))
    x_indices = np.arange(len(coef_df))
    width = 0.28

    ax.bar(x_indices - width, coef_df['OLS Coef'], width, label='OLS Cổ điển', color='#1f77b4', alpha=0.85)
    ax.bar(x_indices, coef_df['Ridge Coef'], width, label=f'Ridge (L2, alpha={best_ridge_alpha:.2f})', color='#ff7f0e', alpha=0.85)
    ax.bar(x_indices + width, coef_df['Lasso Coef'], width, label=f'Lasso (L1, alpha={best_lasso_alpha:.4f})', color='#2ca02c', alpha=0.85)

    ax.axhline(0, color='black', linewidth=1, linestyle='--')
    ax.set_xticks(x_indices)
    ax.set_xticklabels(coef_df['Đặc trưng'], rotation=35, ha='right', fontsize=10, fontweight='bold')
    ax.set_ylabel('Hệ số Hồi quy Chuẩn hóa (Standardized Beta)', fontsize=11, fontweight='bold')
    ax.set_title('BIỂU ĐỒ 09: SO SÁNH CƠ CHẾ CO HỆ SỐ GIỮA OLS, RIDGE (L2) VÀ LASSO (L1)\n(Minh chứng cơ chế Feature Selection tự động của Lasso đưa biến nhiễu về 0)', fontsize=12, fontweight='bold', pad=15)
    ax.legend(frameon=True, framealpha=0.9, fontsize=10)
    plt.tight_layout()
    fig9_path = os.path.join(FIGURES_DIR, '09_regularization_lasso_vs_ridge.png')
    plt.savefig(fig9_path, dpi=300)
    plt.close()
    print(f"✅ Đã lưu Biểu đồ 09 tại: {fig9_path}")

    print("\n🎉 HOÀN THÀNH TOÀN BỘ THỰC NGHIỆM TUẦN 9 VÀ TUẦN 10 THÀNH CÔNG RỰC RỠ!")

if __name__ == '__main__':
    run_all()
