<template>
  <div :class="'app'">
    <registration v-if="page==='reg'" @register="setPage"/>
    <auth v-else-if="token===null" @auth="setToken" @register="setPage"></auth>
    <BoardsList v-else-if="board_id===null" @logedOut="setToken" @showProject="setProject"></BoardsList>
    <KanbanBoard :board="board_id" @back="setProject" @logedOut="setToken" v-else></KanbanBoard>
  </div>
</template>

<script>
import { KanbanBoard, Auth, BoardsList, Registration } from './components';
export default {
  name: "App",
  data() {
    return {
      board_id: null,
      token: null,
      page: null
    }
  },
  components: {
    KanbanBoard,
    BoardsList,
    Auth,
    Registration
  },
  methods: {
    setProject(id) {
      localStorage.setItem('board_id', id)
      this.board_id = id
    },
    setToken() {
      console.log('llo')
      let token = localStorage.getItem("token")
      if(token!==null && token!=="null" && token!==undefined) {
        this.token = token
      } else {
        this.token = null
      }
    },
    setPage(payload) {
      console.log(payload)
      this.page=payload
    }
  },
  mounted() {
    let id = localStorage.getItem('board_id')
    console.log(id)
    if(id!=="null" && id!==null && id!==undefined) {
      this.board_id=id
    }
    this.setToken()
  }
};
</script>

<style src="./style.css"/>

