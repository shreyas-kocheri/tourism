/* ================= CONTRIBUTOR ================= */
function submitContribution() {
  const data = {
    name: document.getElementById("c_name").value,
    state: document.getElementById("c_state").value,
    district: document.getElementById("c_district").value,
    message: document.getElementById("c_message").value
  };

  if (!data.name || !data.state || !data.district || !data.message) {
    alert("Fill all fields");
    return;
  }

  localStorage.setItem("contribution", JSON.stringify(data));
  alert("Update posted");
  window.location.href = "index.html";
}

/* ================= TRAVELLER ================= */
function goToFeed() {
  const state = document.getElementById("stateSelect").value;
  if (!state) {
    alert("Select a state");
    return;
  }
  localStorage.setItem("state", state);
  window.location.href = "feed.html";
}

/* ================= FEED ================= */
function loadFeed() {
  const state = localStorage.getItem("state");
  document.getElementById("title").innerText =
    "📍 " + state + " – Community Updates";

  const box = document.getElementById("posts");
  box.innerHTML = "";

  if (state !== "Uttarakhand") {
    box.innerHTML =
      "<p style='text-align:center'>No updates yet.</p>";
    return;
  }

  let html = `
    <div class="post">
      <b>Dehradun</b>
      <p>Heavy rain reported. Landslide near highway.</p>
      👍 150 | 👎 0
      <div class="trusted">TRUSTED</div>
  `;

  const comments = [
    ["parmila_5689","Heavy rain since early morning",2,21],
    ["md_66ili","Landslide near highway around 6:50 AM",1,18],
    ["cadbury4you","Traffic police diverted vehicles",0,24]
  ];

  comments.forEach(c => {
    html += `
      <div class="comment">
        💬 <b>${c[0]}</b> : ${c[1]}
        <span class="reactions">👎 ${c[2]} | 👍 ${c[3]}</span>
      </div>
    `;
  });

  html += "</div>";
  box.innerHTML = html;
}
