<template>
  <div>
    <div class="d-none d-md-block d-lg-block d-xl-block">
      <div class="btn-active py-3">
        <h3 class="ml-2">
          Admin Panel
        </h3>
      </div>
      <div id="btn1" @click="goDashboard()">
        Dashboard
      </div>
      <div
        id="btn2"
        :class="[btn2_isActive ? 'btn-active' : '']"
        @click="goAccessLog()"
        v-show="!isAdmin"
      >
        Access Log
      </div>
      <div
        id="btn3"
        :class="[btn3_isActive ? 'btn-active' : '']"
        @click="goResetPassword()"
      >
        Reset Password
      </div>
    </div>

    <!-- Mobile -->
    <div class="d-sm-block d-md-none">
      <div class="bg-info py-1 px-1">
        <b-button v-b-toggle.sidebar-1>Toggle Sidebar</b-button>
      </div>
      <b-sidebar id="sidebar-1" title="Admin Panel" shadow>
        <div id="btn1" @click="goDashboard()">
          Dashboard
        </div>
        <div
          id="btn2"
          :class="[btn2_isActive ? 'btn-active' : '']"
          @click="goAccessLog()"
          v-show="!isAdmin"
        >
          Access Log
        </div>
        <div
          id="btn3"
          :class="[btn3_isActive ? 'btn-active' : '']"
          @click="goWebsite()"
        >
          Website
        </div>
      </b-sidebar>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      btn1_isActive: true,
      btn2_isActive: false,
      btn3_isActive: false
    };
  },
  mounted() {
    this.btn1_isActive = true;
    this.btn2_isActiv = false;
    this.btn3_isActive = false;
    this.$router.push("/admin/dashboard");
  },
  methods: {
    goDashboard() {
      this.btn2_isActive = false;
      this.btn3_isActive = false;
      this.btn1_isActive = true;
      this.$router.push("/admin/dashboard");
    },
    goAccessLog() {
      this.btn1_isActive = false;
      this.btn3_isActive = false;
      this.btn2_isActive = true;
      this.$router.push("/admin/access_log");
    },
    goWebsite() {
      this.btn1_isActive = false;
      this.btn2_isActive = false;
      this.btn3_isActive = true;
      this.$router.push("/");
    }
  },
  computed: {
    isAdmin() {
      return this.$store.state.user.a;
    }
  }
};
</script>

<style scoped>
#btn1 {
  padding: 13px 12px;
  color: #7c7c7c;
  border-bottom: 1px solid #b5b5b5;
}
#btn2 {
  padding: 13px 12px;
  color: #7c7c7c;
  border-bottom: 1px solid #b5b5b5;
}
#btn3 {
  padding: 13px 12px;
  color: #7c7c7c;
  border-bottom: 1px solid #b5b5b5;
}
#btn1:hover {
  background-color: #01b7cc;
  color: #fff;
}
#btn2:hover {
  background-color: #01b7cc;
  color: #fff;
}
#btn3:hover {
  background-color: #01b7cc;
  color: #fff;
}
.btn-active {
  background-color: #01b7cc;
  color: #fff !important;
}
</style>
