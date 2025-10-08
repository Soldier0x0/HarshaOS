import axios from 'axios';

export const api = axios.create({
  baseURL: 'http://localhost:9080'
});

export const wsUrl = 'ws://localhost:9080';
