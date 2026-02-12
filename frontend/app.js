const API = "http://127.0.0.1:8000";

async function uploadFile() {

    const file = document.getElementById("fileInput").files[0];

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch(`${API}/upload`, {
        method: "POST",
        body: formData
    });

    const data = await res.json();

    console.log(data);

    renderGrid(data.preview);
}

async function analyzeData() {

    const res = await fetch(`${API}/analyze`, {
        method: "POST"
    });

    const data = await res.json();

    console.log(data);

    document.getElementById("chatBox").innerText =
        JSON.stringify(data, null, 2);
}

function renderGrid(rows){

    let html = "<table border='1'>";

    html += "<tr>";
    Object.keys(rows[0]).forEach(key=>{
        html += `<th>${key}</th>`;
    });
    html += "</tr>";

    rows.forEach(row=>{
        html += "<tr>";
        Object.values(row).forEach(val=>{
            html += `<td>${val}</td>`;
        });
        html += "</tr>";
    });

    html += "</table>";

    document.getElementById("grid").innerHTML = html;
}
