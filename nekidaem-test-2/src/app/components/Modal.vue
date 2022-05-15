<template>
  <div class="modal">
    <div class="modal__content">
        <div class="exit" @click="$emit('close')">x</div>
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "Modal"
}
</script>

<style  scoped>
.modal {
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  position: fixed;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
}
.modal__content {
    margin: auto;
    background: #35383f;
    border-radius: 12px;
    min-height: 50px;
    min-width: 300px;
    max-width: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    flex-direction: column;
  }
  @media (max-width: 400px) {
      .modal__content {
        max-width: 80%;
      }
    }

    .exit {
        position: absolute;
        left: 10px;
        top: 10px;
        font-size: 20px;
        color: #c4c4c4;
    }
</style>