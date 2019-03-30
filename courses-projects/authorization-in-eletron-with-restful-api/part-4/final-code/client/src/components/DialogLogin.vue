<template>
    <v-dialog v-model="!this.$store.state.auth_login" persistent max-width="600px">
        <v-card>
            <v-card-title>Account login</v-card-title>

            <v-card-text>
                <v-form>
                    <v-container grid-list-md>
                        <v-text-field label="E-mail" v-model="username"></v-text-field>
                        <v-text-field label="Password" v-model="password"></v-text-field>

                        <v-checkbox v-model="remeber_login" label="Remeber my login on this computer"></v-checkbox>
                    </v-container>
                </v-form>
            </v-card-text>

            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" flat @click="auth_login">Login</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
    export default {
        name: "DialogLogin",
        data () {
            return {
                username: '',
                password: '',
                remeber_login: false
            }
        },

        methods: {
            auth_login () {
                console.log('hit login btn')

                this.$store.commit('account_sign_in', {
                    username: this.username,
                    password: this.password,
                    remeber_login: this.remeber_login
                })

                this.username = '';
                this.password = '';
                this.remeber_login = false;
            }
        }
    }
</script>

<style scoped>

</style>