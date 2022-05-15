<template>
<div class="projects">
    <div class="userinfo">
			<div class="username">
				Вы вошли как {{ username }}
			</div>
			<button class="back-btn logout-btn" @click="logout">Выйти</button>
		</div>
  <div class="page_header">Ваши проекты:</div>
  <div class="projects_list" v-if="boards">
    <div class="project" v-for="board in boards" :key="board.id" @click="$emit('showProject', board)">
      {{board.name}}
    </div>
    <div class="project project_add" @click="showModal">+</div>
  </div>
  <Modal v-if="modal" @close="showModal" class="projects_create">
    <h1>Название проекта</h1>
     <input type="text" v-model="name" class="card-title-textarea" placeholder="Название проекта">
     <button type="button" class="add-a-card"  @click="createProject">Создать</button>
  </Modal>
</div>
</template>

<script>
import Modal from "./Modal.vue"
import optionsMixin from '../mixins/optionsMixin'
import {getBoards, createBoard} from '@/services/api'

export default {
    name: "BoardsList",
    components: {Modal},
    mixins: [optionsMixin],
    data() {
        return {
            boards: [],
            modal: false,
            name: "",
        };
    },
    methods: {
        getBoards() {
            getBoards(this.user, this.options).then(res => {
                this.boards = res.data;
            }).catch(err => {
                console.log((err));
            });
        },
        showModal() {
            this.modal = !this.modal;
        },
        createProject() {
          createBoard(
          {
            "name": this.name,
            "author": this.user
          },
          this.options
          ).then(() => {
                this.showModal()
                this.getBoards()
            }).catch(err => {
                console.log((err));
            });
        },
    },
    created() {
        this.getBoards();
    },
}
</script>

