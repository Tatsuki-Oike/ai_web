<script setup lang="ts">

import { ref } from "vue"
import axios from 'axios'

const textInput = ref<string>("");
const textOutput = ref<string>("");
const loading = ref<boolean>(false);
const errorFlg = ref<boolean>(false);


const submitForm = async (): Promise<void> => {

  if (textInput.value.trim() !== "") {

    textOutput.value = ""
    loading.value = true
    errorFlg.value = false

    const postData = {
      "input_text": textInput.value
    }

    try {

      const response = await axios.post('http://127.0.0.1:5000/api/translation', postData);
      textOutput.value = response.data.output_text;

    } catch (error) {
      errorFlg.value = true
      console.error(error);
    }

    loading.value = false
  }

};

</script>

<template>

    <form>
      <div class="mt-4">
        <label for="exampleInput" class="form-label h2">日本語を入力してください:</label>
        <input type="text" class="form-control" id="exampleInput" v-model="textInput">
      </div>
      <button type="button" class="btn btn-primary mt-3" @click="submitForm">Submit</button>
    </form>

    <div v-if="loading" class="mt-3">
      <p class="alert alert-dark d-flex align-items-center">
        <div class="spinner-border me-2 text-dark" role="status"></div>
          翻訳中
      </p>
    </div>

    <div v-if="errorFlg">
      翻訳でERRORが発生しました。
    </div>
    <div v-else-if="textOutput" class="text-center">
      <div class="card my-5">
        <div class="card-header">
          <h2 class="card-title fs-2">翻訳結果</h2>
        </div>
        <div class="card-body fs-4">
          {{ textOutput }}
        </div>
      </div>
    </div>

</template>

