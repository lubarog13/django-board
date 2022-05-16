export default {
    data() {
        return {
            user: localStorage.getItem("user_id"),
            username: localStorage.getItem("username"),
            options: {
				headers: {
					"Authorization": "Token " + localStorage.getItem('token')
				}
			},
        }
    },
    methods: {
        logout() {
            localStorage.removeItem("token")
            localStorage.removeItem("user_id")
            localStorage.removeItem("username")
            localStorage.removeItem("board_id")
            localStorage.setItem('board_id', null)
            this.$emit("logedOut")
        },
    }
}
