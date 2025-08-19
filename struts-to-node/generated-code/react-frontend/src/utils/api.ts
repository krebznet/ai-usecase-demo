import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:3001/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for auth tokens
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('authToken');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('authToken');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export const welcome = async () => {
  const response = await api.get('/welcome');
  return response.data;
};

export const applicantInfo = async (data: any) => {
  const response = await api.post('/applicantInfo', data);
  return response.data;
};

export const vehiclePreference = async (data: any) => {
  const response = await api.post('/vehiclePreference', data);
  return response.data;
};

export const financialInfo = async (data: any) => {
  const response = await api.post('/financialInfo', data);
  return response.data;
};

export const backgroundCheck = async (data: any) => {
  const response = await api.post('/backgroundCheck', data);
  return response.data;
};

export const leaseReview = async () => {
  const response = await api.get('/leaseReview');
  return response.data;
};

export const submitApplication = async () => {
  const response = await api.get('/submitApplication');
  return response.data;
};

export default api;
