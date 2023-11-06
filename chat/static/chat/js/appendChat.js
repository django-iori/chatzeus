import { endpoint } from "./env.js";
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const target = document.querySelector('.card-body');
const form = document.getElementById("form");
form.addEventListener('submit', async(e) => {
  e.preventDefault();
  // chat内容を取得
  const input = document.querySelector('input[type="text"]');
  postData(input.value);
});

async function postData(text) {
  // 現在時刻を取得
  const date = new Date();
  const datetime = `${date.getHours()}:${date.getMinutes()}`;

  // APIへのリクエストを表示
  const div = document.createElement('div');
  div.innerHTML = `
    <div class="d-flex flex-row justify-content-end mb-4 pt-1">
      <div>
        <p class="small p-2 me-3 mb-1 text-white rounded-3 bg-primary">${text}</p>
        <p class="small me-3 mb-3 rounded-3 text-muted d-flex justify-content-end">${datetime}</p>
      </div>
      <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava4-bg.webp"
        alt="avatar 1" style="width: 45px; height: 100%;">
    </div>
  `;
  target.appendChild(div);
  target.scrollIntoView({ block: "end" });
  
  // APIにリクエストを送信
  const body = new FormData()
  body.append('content', text)

  fetch(endpoint, {
    method: 'POST',
    headers: {
      'X-CSRFToken': csrftoken,
    },
    mode: 'same-origin',
    body: body
  })
  .then(response => response.json())
  .then(data => {
    // APIからのレスポンスを表示
    const div = document.createElement('div');
    div.innerHTML = `
      <div class="d-flex flex-row justify-content-start">
        <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3-bg.webp"
          alt="avatar 1" style="width: 45px; height: 100%;">
        <div>
          <p class="small p-2 ms-3 mb-1 rounded-3" style="background-color: #f5f6f7;">${data.message}</p>
          <p class="small ms-3 mb-3 rounded-3 text-muted">${datetime}</p>
        </div>
      </div>
    `;
    target.appendChild(div);
    target.scrollIntoView({ block: "end" });
  })
  .catch(error => {
    console.error('Error:', error);
    return error;
  });
}


