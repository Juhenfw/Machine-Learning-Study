from sklearn.cluster import KMeans

# Buat model KMeans Scikit-Learn
sklearn_clt = KMeans(n_clusters=5, max_iter=300, random_state=0)
sklearn_clt.fit(X)

# Prediksi hasil klasterisasi
y_pred_sklearn = sklearn_clt.predict(X)
centers_pred_sklearn = sklearn_clt.cluster_centers_

# Visualisasikan prediksi
fig, ax = plt.subplots(figsize=(10, 8))
sc = ax.scatter(X[:, 0], X[:, 1], c=y_pred_sklearn, cmap='viridis', marker='o')
sc_centers = ax.scatter(centers_pred_sklearn[:, 0], centers_pred_sklearn[:, 1], c='red', marker='x', s=200)
plt.xlabel('NMHC')
plt.ylabel('RH')
plt.title('Air Quality Data Clustering with K-Means (5 Clusters)')
plt.colorbar(sc, label='Cluster Label')
plt.show()

# Mendapatkan nilai cluster errors
clt.return_wcss()

# Menghitung jarak setiap titik data ke centroid klasternya
cluster_assignment = clt.predict(X)
mae_values = []

for i in range(clt.K):
    # Ambil titik data yang berada dalam cluster i
    cluster_points = X[cluster_assignment == i]
    # Hitung jarak setiap titik dalam cluster ini ke centroid-nya
    centroid = centers_pred[i]
    mae_cluster = mean_absolute_error(cluster_points, np.tile(centroid, (cluster_points.shape[0], 1)))
    mae_values.append(mae_cluster)

# Menghitung rata-rata MAE di seluruh cluster
overall_mae = np.mean(mae_values)
print(f"Mean Absolute Error (MAE) across clusters: {overall_mae:.4f}")

# Kalibrasikan pelabelan (if needed)
# (Kalibrasi ini tidak diperlukan jika tidak ada label asli)

# Evaluasi kualitas klasterisasi menggunakan Silhouette Score
silhouette_avg = silhouette_score(X, y_pred)
print(f'Silhouette Score: {silhouette_avg:.4f}')

# Evaluasi performa
# mae_sklearn = mean_absolute_error(centers, centers_pred_sklearn)
acc_sklearn = accuracy_score(y, y_pred_sklearn)
pre_sklearn = precision_score(y, y_pred_sklearn, average='weighted')
rec_sklearn = recall_score(y, y_pred_sklearn, average='weighted')
f1_sklearn = f1_score(y, y_pred_sklearn, average='weighted')

# print(f"MAE (Scikit-Learn KMeans): {mae_sklearn:.4f}")
print(f"Accuracy (Scikit-Learn KMeans): {acc_sklearn:.4f}")
print(f"Precision (Scikit-Learn KMeans): {pre_sklearn:.4f}")
print(f"Recall (Scikit-Learn KMeans): {rec_sklearn:.4f}")
print(f"F1 Score (Scikit-Learn KMeans): {f1_sklearn:.4f}")
