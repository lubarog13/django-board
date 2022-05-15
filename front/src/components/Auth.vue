<template>
    <div class="auth">
        <FormulateForm @submit="onSubmit" v-model="form">
            <h3>Войдите в аккаунт</h3>
            <FormulateInput
                type="text"
                name="login"
                validation="required"
                placeholder="Ваш логин"
            />
            <FormulateInput validation="required" type="password" name="password" placeholder="Пароль"/>
            <p class="error" v-if="error">Ошибка входа в систему. Проверьте логин и пароль</p>
            <div class="form-actions">
            <FormulateInput type="submit" class="login-button" label="Войти"></FormulateInput>
            <button type="button" class="register-button" @click="$emit('register', 'reg')">Регистрация</button>
            </div>
        </FormulateForm>
    </div>
</template>

<script>
import axios from "axios"
    export default {
        name: "Auth",
        data() {
            return {
                form: {
                    login: null,
                    password: null,
                },
                error: null
            }
        },
        methods: {
            onSubmit() {
                axios.post(`http://0.0.0.0:8000/api-token-auth/`,{ username: this.form.login, password: this.form.password }).then(res => {
					localStorage.setItem("token", res.data.token)
                    const options = {
                        headers: {
                            "Authorization": "Token " + localStorage.getItem('token')
                        }   
                    }
                    axios.get(`http://0.0.0.0:8000/users/me/`, options).then(res => {
                        localStorage.setItem("user_id", res.data.id)
                        localStorage.setItem("username", res.data.username)
                        this.$emit('auth')
                    }).catch(err => {
                        console.log(err)
                        this.error = true
                    })
				}).catch(err => {
                    console.log(err)
                    this.error = true
                })
            }
        }
    }
</script>
