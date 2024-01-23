from sklearn.preprocessing import PolynomialFeatures

# Original feature vector
X = [[1, 2]]

# Create PolynomialFeatures object with degree=2
poly = PolynomialFeatures(degree=2)

# Transform the original features
X_poly = poly.fit_transform(X)

# The transformed feature vector
print(X_poly)