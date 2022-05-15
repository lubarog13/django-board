import axios from 'axios'

const baseURL = "http://0.0.0.0:8000"


export async function auth(data) {
    return axios.post(`${baseURL}/api-token-auth/`,data)
}

export async function signUp(data) {
    return axios.post(`${baseURL}/registration/`, data)
}

export async function getMe(options) {
    return axios.get(`${baseURL}/users/me/`, options)
}

export async function getBoards(user, options) {
    return axios.get(`${baseURL}/boards/${user}/`, options)
}

export async function createBoard(data, options) {
    return axios.post(`${baseURL}/board/`, data, options)
}

export async function getCards(board, progress, options) {
    return axios.get(`${baseURL}/board/${board}/cards/${progress}`, options)
}

export async function updateCard(id, data, options) {
    return axios.put(`${baseURL}/cards/${id}/`, data, options)
}
export async function addCard(data, options) {
    return axios.post(`${baseURL}/card/`,data, options)
}

export async function deleteCard(id, options) {
    return axios.delete(`${baseURL}/cards/${id}`, options)
}

export async function changeBoard(id, data ,options) {
    return axios.put(`${baseURL}/boards/${id}/`, data, options)
}

export async function deleteBoard(id, options) {
    return axios.delete(`${baseURL}/boards/${id}/`, options)
}
