<template>
    <div class="auth">
        <FormulateForm @submit="onSubmit" v-model="form">
            <h3>Регистрация</h3>
            <FormulateInput
                type="text"
                name="login"
                validation="required"
                placeholder="Введите логин"
            />
            <FormulateInput
                type="email"
                name="email"
                validation="required|email"
                placeholder="Введите email"
            />
            <FormulateInput validation="required|min:8" type="password" name="password" placeholder="Пароль"/>
            <FormulateInput validation="required|confirm" type="password" name="password_confirm" placeholder="Повторите пароль"  validation-name="Confirmation"/>
            <p class="error" v-if="error">Ошибка регистрации, проверьте поля</p>
            <div class="form-actions">
            <FormulateInput type="submit" class="login-button" label="Зарегестрироваться"></FormulateInput>
            <button type="button" class="register-button" @click="$emit('register', null)">Войти</button>
            </div>
        </FormulateForm>
    </div>
</template>

<script>
import {signUp} from "../services/api"
    export default {
        name: "Registration",
        data() {
            return {
                form: {
                    login: null,
                    password: null,
                    email: null
                },
                error: null
            }
        },
        methods: {
            onSubmit() {
                signUp({ username: this.form.login, email: this.form.email, password: this.form.password }).then(() => {
					this.$toast.success('Profile saved.', {
                        position: "bottom"
                    })
                    this.$emit("register", null)
				}).catch(err => {
                    console.log(err)
                    this.error = true
                })
            }
        }
    }
</script>
