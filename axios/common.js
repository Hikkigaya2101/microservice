
// frontend/src/api/common.js
import axios from 'axios'

export const HTTP = axios.create({
  baseURL: '/api/'
})