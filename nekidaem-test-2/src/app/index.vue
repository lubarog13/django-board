<template>
  <div :class="'app'">
    <BoardsList v-if="board_id===null" @showProject="setProject"></BoardsList>
    <KanbanBoard :board="board_id" @back="setProject" v-else></KanbanBoard>
  </div>
</template>

<script>
import { KanbanBoard } from './components';
import BoardsList from "./components/BoardsList";
export default {
  name: "App",
  data() {
    return {
      board_id: null
    }
  },
  components: {
    KanbanBoard,
    BoardsList
  },
  methods: {
    setProject(id) {
      localStorage.setItem('board_id', id)
      this.board_id = id
    }
  },
  mounted() {
    let id = localStorage.getItem('board_id')
    console.log(id)
    if(id!=="null" && id!==null && id!==undefined) {
      this.board_id=id
    }
  }
};
</script>

<style src="../style.css"/>

