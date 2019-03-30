<template>
  <v-app>
    <v-navigation-drawer fixed app>
      <v-toolbar flat>
        <v-list>
          <v-list-tile class="title">
            Application
          </v-list-tile>
        </v-list>
      </v-toolbar>

      <v-divider></v-divider>

      <v-list dense>
        <v-list-tile @click="">
          <v-list-tile-action>
            <v-icon>dashboard</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Dashboard</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

        <v-list-tile @click="auth_sign_out">
          <v-list-tile-action>
            <v-icon>lock_open</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Sign out</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>

      <div align="center">
        <small>version alpha 0.0.1</small>
      </div>
    </v-navigation-drawer>

    <v-content>
      <v-container fuild>
      <router-view></router-view>
      </v-container>
    </v-content>

    <DialogLogin />
  </v-app>
</template>

<script>
  import DialogLogin from './components/DialogLogin';

export default {
  name: 'App',
  components: {
    DialogLogin
  },
  data () {
    return {
      //
    }
  },
  methods: {
    auth_sign_out () {
      this.$store.commit('account_sign_out');
    }
  }
}
</script>
