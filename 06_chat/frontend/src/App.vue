<script setup lang="ts">

import { ref } from "vue"
import axios from 'axios'

type PostType = {
  "person": string,
  "content": string
}

const textInput = ref<string>("");
const textOutput = ref<string>("");
const messages = ref<PostType[]>([])
const loading = ref<boolean>(false);
const errorFlg = ref<boolean>(false);

const submitForm = async (): Promise<void> => {
  if (textInput.value.trim() !== "") {
    messages.value.push(
      {
        "person": "me",
        "content": textInput.value
      }
    )
    textOutput.value = ""
    loading.value = true
    errorFlg.value = false

    const postData = {
      "input_text": textInput.value
    }

    try {

      const response = await axios.post('http://127.0.0.1:5000/api/chat', postData);
      textOutput.value = response.data.output_text;
      messages.value.push({
        "person": "you",
        "content": textOutput.value
      })

    } catch (error) {
      errorFlg.value = true
      console.error(error);
    }

    loading.value = false
    textInput.value = ""
  }
};

</script>

<template>

    <form>
      <div class="mt-4">
        <label for="exampleInput" class="form-label h2">English Chat:</label>
        <input type="text" class="form-control" id="exampleInput" v-model="textInput">
      </div>
      <button type="button" class="btn btn-primary mt-3" @click="submitForm">Submit</button>
    </form>

    <div v-if="loading" class="mt-3">
      <p class="alert alert-dark d-flex align-items-center">
        <div class="spinner-border me-2 text-dark" role="status"></div>
          返信中
      </p>
    </div>

    <div v-if="errorFlg">
      返信中にERRORが発生しました。
    </div>
    
    <div v-else-if="messages" class="text-center my-3">
      <template v-for="msg in messages">

        <template v-if="msg.person==='me'">
          <div class="d-flex justify-content-end">
            <div class="card text-bg-success mb-3" style="max-width: 60%;">
              <div class="card-body px-4">
                {{ msg.content }}
              </div>
            </div>
          </div>
        </template>

        <template v-else>
          <div class="d-flex justify-content-start">
            <div class="card text-bg-light mb-3" style="max-width: 60%;">
              <div class="card-body px-4">
                {{ msg.content }}
              </div>
            </div>
          </div>
        </template>

      </template>
    </div>

</template>