const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;

export const getVendors = () => {
  const url = `${API_BASE_URL}/vendors`;
  return fetch(url).then(res => res.json());
};

export const getProducts = vendorId => {
  const url = `${API_BASE_URL}/vendors/${vendorId}/products`;
  return fetch(url).then(res => res.json());
};

export const getOrders = (vendorId, productId) => {
  const url = (
    `${API_BASE_URL}/vendors/${vendorId}/products/${productId}/orders`
  );
  return fetch(url).then(res => res.json());
};
