const button = document.querySelector('button');
button.addEventListener('click', (e) => {
  const div = document.createElement('div');
  div.innerHTML = `
    <div class="d-flex flex-row justify-content-end mb-4 pt-1">
      <div>
        <p class="small p-2 me-3 mb-1 text-white rounded-3 bg-primary">${e.target.innerText}</p>
        <p class="small p-2 me-3 mb-1 text-white rounded-3 bg-primary">How are you doing?</p>
        <p class="small p-2 me-3 mb-1 text-white rounded-3 bg-primary">Long time no see! Tomorrow office. will be free on sunday.</p>
        <p class="small me-3 mb-3 rounded-3 text-muted d-flex justify-content-end">00:06</p>
      </div>
      <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava4-bg.webp"
        alt="avatar 1" style="width: 45px; height: 100%;">
    </div>
  `;
  const target = document.querySelector('.card-body');
  target.appendChild(div);
});
