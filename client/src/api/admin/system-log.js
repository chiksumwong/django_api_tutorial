import Vue from "vue";

const SystemLogAPI = {
  //List
  listSystemLogs: () => Vue.prototype.$axios.get("/f/log/"),
  createSystemLog: payload => Vue.prototype.$axios.post("/f/log/", payload),
  //Detail
  retrieveSystemLog: system_logId =>
    Vue.prototype.$axios.get("/f/log/" + system_logId + "/"),
  updateSystemLog: (system_logId, payload) =>
    Vue.prototype.$axios.put("/f/log/" + system_logId + "/", payload),
  deleteSystemLog: system_logId =>
    Vue.prototype.$axios.delete("/f/log/" + system_logId + "/")
};

export default SystemLogAPI;
