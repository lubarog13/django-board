<template>
	<div class="kanban-board">
		<button class="back-btn" @click="$emit('back', null)">Назад</button>
		<div class="row"  v-if="items0">
			<h3 class="header orange">On Hold ({{items0.length}})</h3>
			<Container :group-name="'1'" :get-child-payload="getChildPayload0" @drop="onDrop('items0', $event)">
				<Draggable v-for="item in items0" :key="item.id">
					<div class="draggable-item">
						<div class="delete" @click="deleteItem('items0', item)"></div>
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
			<Container :group-name="'1'" :get-child-payload="getChildPayload1" @drop="onDrop('items1', $event)">
				<Draggable v-for="item in items1" :key="item.id">
					<div class="draggable-item">
						<div class="delete" @click="deleteItem('items1', item)"></div>
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
			<Container :group-name="'1'" :get-child-payload="getChildPayload2" @drop="onDrop('items2', $event)"> 
				<Draggable v-for="item in items2" :key="item.id">
					<div class="draggable-item">
						<div class="delete" @click="deleteItem('items2', item)"></div>
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
			<Container :group-name="'1'" :get-child-payload="getChildPayload3" @drop="onDrop('items3', $event)">
				<Draggable v-for="item in items3" :key="item.id">
					<div class="draggable-item">
						<div class="delete" @click="deleteItem('items3', item)"></div>
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
	</div>
</template>

<script>
import axios from 'axios';
import { Container, Draggable } from "vue-smooth-dnd";
import { applyDrag } from "./utils";
export default {
	name: "KanbanBoard",
	components: { Container, Draggable },
	props: ["board"],
	data: function() {
		return {
			items0: null,
			items1: null,
			items2: null,
			items3: null,
			newCardHeader: '',
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
			return axios.get(`http://0.0.0.0:8000/board/${this.board}/cards/${progress}`).then(res => {
				this[collection] = res.data
			}).catch(err => {
				console.log(err)
			})
		},
		setItems() {
			this.loadItems('onHold', 'items0')
			this.loadItems('inProgress', 'items1')
			this.loadItems('needsReview', 'items2')
			this.loadItems('approved', 'items3')
		},
		onDrop: function(collection, dropResult) {
			this.hideAddACardTextarea();
			this[collection] = applyDrag(this[collection], dropResult);
			saveItems(collection, this[collection]);
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
				 axios.post(`http://0.0.0.0:8000/card/`, {title: this.newCardHeader, progress: progress, board: this.board, order: this[collection].length}).then(res => {
					 this[collection].push(res.data)
				 }).catch(err => {
					 console.log(err)
				 })
				this.hideAddACardTextarea();
			}
		},
		deleteItem: function(collection, item) {
			let index = this[collection].map(x => {
				return x.id;
			}).indexOf(item.id);
			this[collection].splice(index, 1);
			saveItems(collection, this[collection]);
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