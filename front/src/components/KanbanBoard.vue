<template>
	<div class="kanban-board">
		<button class="back-btn" @click="$emit('back', null)">Назад</button>
		<div class="userinfo">
			<div class="username">
				Вы вошли как {{ username }}
			</div>
			<button class="back-btn logout-btn" @click="logout">Выйти</button>
		</div>
    <div class="heading">
      <input class="editName" type="text" v-on:keyup.enter="changeName" v-model="newName" placeholder="Название проекта" v-if="editBoard">
      <h1 v-else>{{boardName}}</h1>
      <font-awesome-icon icon="fa-solid fa-pencil-square" @click="editBoard=!editBoard"/>
      <font-awesome-icon icon="fa-solid fa-trash" @click="showModal"/>
    </div>
		<div class="row"  v-if="items0">
			<h3 class="header orange">On Hold ({{items0.length}})</h3>
			<Container :group-name="'1'" :get-child-payload="getChildPayload0" @drop="onDrop('items0', $event, 'onHold')">
				<Draggable v-for="item in items0" :key="item.id">
					<div class="draggable-item">
						<div class="delete" @click="deleteItem('items0', item, 'onHold')"></div>
						<p><b class="id">id: </b>{{item.id}}</p>
						<p>{{item.title}}</p>
					</div>
				</Draggable>
			</Container>
			<textarea id="title0" class="card-title-textarea" rows="5" placeholder="Ввести заголовок для этой карточки" v-model="newCardHeader" v-bind:style="addACardStyle[0]"></textarea>
			<button class="add-a-card" @click="addItem('items0', 'onHold')" v-bind:style="addACardStyle[0]">Добавить карточку</button>
			<button class="cancel" @click="hideAddACardTextarea()" v-bind:style="addACardStyle[0]"></button>
			<button class="add-another-card" @click="showAddACardTextarea(0)" v-bind:style="addAnotherCardStyle[0]">Добавить карточку</button>
		</div>
		<div class="row" v-if="items1">
			<h3 class="header blue">In Progress ({{items1.length}})</h3>
			<Container :group-name="'1'" :get-child-payload="getChildPayload1" @drop="onDrop('items1', $event, 'inProgress')">
				<Draggable v-for="item in items1" :key="item.id">
					<div class="draggable-item">
						<div class="delete" @click="deleteItem('items1', item, 'inProgress')"></div>
						<p><b class="id">id: </b>{{item.id}}</p>
						<p>{{item.title}}</p>
					</div>
				</Draggable>
			</Container>
			<textarea id="title1" class="card-title-textarea" rows="5" placeholder="Ввести заголовок для этой карточки" v-model="newCardHeader" v-bind:style="addACardStyle[1]"></textarea>
			<button class="add-a-card" @click="addItem('items1', 'inProgress')" v-bind:style="addACardStyle[1]">Добавить карточку</button>
			<button class="cancel" @click="hideAddACardTextarea()" v-bind:style="addACardStyle[1]"></button>
			<button class="add-another-card" @click="showAddACardTextarea(1)" v-bind:style="addAnotherCardStyle[1]">Добавить карточку</button>
		</div>
		<div class="row" v-if="items2">
			<h3 class="header yellow">Needs Review ({{items2.length}})</h3>
			<Container :group-name="'1'" :get-child-payload="getChildPayload2" @drop="onDrop('items2', $event, 'needsReview')">
				<Draggable v-for="item in items2" :key="item.id">
					<div class="draggable-item">
						<div class="delete" @click="deleteItem('items2', item, 'needsReview')"></div>
						<p><b class="id">id: </b>{{item.id}}</p>
						<p>{{item.title}}</p>
					</div>
				</Draggable>
			</Container>
			<textarea id="title2" class="card-title-textarea" rows="5" placeholder="Ввести заголовок для этой карточки" v-model="newCardHeader" v-bind:style="addACardStyle[2]"></textarea>
			<button class="add-a-card" @click="addItem('items2', 'needsReview')" v-bind:style="addACardStyle[2]">Добавить карточку</button>
			<button class="cancel" @click="hideAddACardTextarea()" v-bind:style="addACardStyle[2]"></button>
			<button class="add-another-card" @click="showAddACardTextarea(2)" v-bind:style="addAnotherCardStyle[2]">Добавить карточку</button>
		</div>
		<div class="row" v-if="items3">
			<h3 class="header green">Approved ({{items3.length}})</h3>
			<Container :group-name="'1'" :get-child-payload="getChildPayload3" @drop="onDrop('items3', $event, 'approved')">
				<Draggable v-for="item in items3" :key="item.id">
					<div class="draggable-item">
						<div class="delete" @click="deleteItem('items3', item, 'approved')"></div>
						<p><b class="id">id: </b>{{item.id}}</p>
						<p>{{item.title}}</p>
					</div>
				</Draggable>
			</Container>
			<textarea id="title3" class="card-title-textarea" rows="5" placeholder="Ввести заголовок для этой карточки" v-model="newCardHeader" v-bind:style="addACardStyle[3]"></textarea>
			<button class="add-a-card" @click="addItem('items3', 'approved')" v-bind:style="addACardStyle[3]">Добавить карточку</button>
			<button class="cancel" @click="hideAddACardTextarea()" v-bind:style="addACardStyle[3]"></button>
			<button class="add-another-card" @click="showAddACardTextarea(3)" v-bind:style="addAnotherCardStyle[3]">Добавить карточку</button>
		</div>
    <Modal v-if="modal" @close="showModal" class="projects_delete projects_create">
      <h1>Вы действительно хотите удалить  <br/> проект?</h1>
      <p>Отменить это действие будет невозможно</p>
      <button type="button" class="add-a-card"  @click="deleteProject">Удалить</button>
    </Modal>
	</div>
</template>

<script>
import { Container, Draggable } from "vue-smooth-dnd";
import Modal from "@/components/Modal";
import { applyDrag } from "./utils";
import { getCards, updateCard, addCard, deleteCard, changeBoard, deleteBoard } from '@/services/api'
import optionsMixin from '../mixins/optionsMixin'
export default {
	name: "KanbanBoard",
	components: { Container, Draggable, Modal },
	mixins: [optionsMixin],
	props: ["board"],
	data: function() {
		return {
			items0: null,
			items1: null,
			items2: null,
			items3: null,
			newCardHeader: '',
      editBoard: false,
      modal: false,
      boardName: localStorage.getItem("boardName"),
      newName: localStorage.getItem("boardName"),
			addACardStyle: [
					{ display: 'none'},
					{ display: 'none'},
					{ display: 'none'},
					{ display: 'none'}
				],
			addAnotherCardStyle: [
					{ display: 'block'},
					{ display: 'block'},
					{ display: 'block'},
					{ display: 'block'}
				]
		};
	},
	methods: {
		async loadItems(progress, collection) {
			return getCards(this.board, progress, this.options).then(res => {
				this[collection] = res.data
			}).catch(err => {
				console.log(err)
			})
		},
    showModal() {
      this.modal = !this.modal;
    },
		setItems() {
			this.loadItems('onHold', 'items0')
			this.loadItems('inProgress', 'items1')
			this.loadItems('needsReview', 'items2')
			this.loadItems('approved', 'items3')
		},
		onDrop: function(collection, dropResult, progress) {
			this.hideAddACardTextarea();
			console.log(collection, dropResult)
			this[collection] = applyDrag(this[collection], dropResult);
			if (dropResult.addedIndex!==null) {
				dropResult.payload.progress = progress
				dropResult.payload.order = this[collection].indexOf(dropResult.payload)
				updateCard(dropResult.payload.id, dropResult.payload, this.options).catch(err => {
					console.log(err)
				})
				return
			}
			if(dropResult.removedIndex!==null) {
				this[collection].forEach((element, index) => {
					if (index>dropResult.removedIndex) {
						element.order -= 1
						updateCard(element.id,element, this.options).catch(err => {
							console.log(err)
						})
					}
				});
			}
		},
    changeName() {
      if (this.newName.length===0){
        this.editBoard = false
        return
      }
      changeBoard(this.board, {name: this.newName, author: this.user}, this.options).then(() => {
        this.boardName = this.newName
        localStorage.setItem("boardName", this.newName)
      }).catch(err => {
        console.log(err)
      }).finally(() => {
        this.editBoard = false
      })
    },
    deleteProject() {
      deleteBoard(this.board, this.options).then(() => {
        this.$emit('back', null)
      }).catch(err => {
        console.log(err)
      })
    },
		getChildPayload0: function(index) {
			return this.items0[index];
		},
		getChildPayload1: function(index) {
			return this.items1[index];
		},
		getChildPayload2: function(index) {
			return this.items2[index];
		},
		getChildPayload3: function(index) {
			return this.items3[index];
		},
		addItem: function(collection, progress) {
			if (this.newCardHeader) {
				addCard({title: this.newCardHeader, progress: progress, board: this.board, order: this[collection].length}, this.options).then(res => {
					this[collection].push(res.data)
				}).catch(err => {
					console.log(err)
				})
				this.hideAddACardTextarea();
			}
		},
		deleteItem: function(collection, item, progress) {
			deleteCard(item.id, this.options).then(() => {
					this.loadItems(progress, collection)
				}).catch(err => {
					console.log(err)
				})
		},
		hideAddACardTextarea: function() {
			this.newCardHeader = '';
			for(let i = 0; i < this.addACardStyle.length; i++) {
				this.addACardStyle[i].display = 'none';
			}
			for(let i = 0; i < this.addAnotherCardStyle.length; i++) {
				this.addAnotherCardStyle[i].display = 'block';
			}
		},
		showAddACardTextarea: function(col) {
			this.hideAddACardTextarea();
			this.addAnotherCardStyle[col].display = 'none';
			this.addACardStyle[col].display = 'block';
			let textareaID = 'title' + col;

			setTimeout(function() {
				document.getElementById(textareaID).focus();
			}, 0);
		}
	},
	created() {
		this.setItems()
	}
};
</script>
