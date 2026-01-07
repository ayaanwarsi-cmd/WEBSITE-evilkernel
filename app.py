from flask import Flask, Response

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>EviLKeRneL | SQLMap Automation Ecosystem</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
:root{
  --bg:#020b07;
  --glass:rgba(18, 40, 28, 0.65);
  --border:rgba(90,255,180,0.25);
  --accent:#11e87d;
  --text:#39ff70;
  --muted:#9fffcf;
}

*{box-sizing:border-box}

body{
  margin:0;
  background:#020b07;
  color:var(--text);
  font-family:"Segoe UI", monospace;
  overflow-x:hidden;
}

/* MATRIX CANVAS */
canvas{
  position:fixed;
  inset:0;
  z-index:-1;
}

/* GLASS */
.glass{
  background:var(--glass);
  backdrop-filter: blur(18px);
  border:1px solid var(--border);
  border-radius:18px;
  box-shadow:0 0 50px rgba(17,232,125,0.18);
}

/* HEADER */
header{
  min-height:100vh;
  display:flex;
  align-items:center;
  justify-content:center;
  padding:40px 20px;
}

.hero{
  max-width:980px;
  padding:60px;
  text-align:center;
}

.hero h1{
  font-size:54px;
  margin:0;
  color:#aaffd9;
  letter-spacing:3px;
}

/* TERMINAL */
.terminal{
  margin:25px auto;
  background:#000;
  border-radius:12px;
  padding:20px;
  text-align:left;
  max-width:700px;
  color:#39ff70;
  box-shadow:0 0 30px rgba(0,255,140,.3);
}

/* BUTTON */
.btn{
  display:inline-block;
  padding:15px 32px;
  margin:10px;
  border-radius:999px;
  background:linear-gradient(135deg,#11e87d,#5affb4);
  color:#02140a;
  font-weight:900;
  text-decoration:none;
  letter-spacing:1px;
  box-shadow:0 0 30px rgba(17,232,125,.55);
  cursor:pointer;
}

/* SECTIONS */
section{
  max-width:1200px;
  margin:0 auto 130px;
  padding:0 22px;
}

h2{
  color:#aaffd9;
  font-size:34px;
}

/* GRID */
.grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
  gap:26px;
}

.card{
  padding:30px;
}

.price{
  font-size:28px;
  color:#7dffb0;
}

/* MODAL */
.modal{
  position:fixed;
  inset:0;
  background:rgba(0,0,0,.8);
  display:none;
  align-items:center;
  justify-content:center;
  z-index:999;
}

.modal-content{
  max-width:400px;
  padding:30px;
  text-align:center;
}

input{
  width:100%;
  padding:12px;
  margin:10px 0;
  border:none;
  border-radius:6px;
}

/* FOOTER */
footer{
  text-align:center;
  padding:40px;
  border-top:1px solid var(--border);
}
</style>
</head>

<body>

<canvas id="matrix"></canvas>

<header>
  <div class="hero glass">
    <h1>EviLKeRneL</h1>

    <div class="terminal">
      <pre id="typing"></pre>
    </div>

    <a class="btn" onclick="location.href='https://t.me/EviLKeRneLfreeTOOLS'">FREE TOOLS</a>
    <a class="btn" onclick="location.href='https://t.me/EviLKeRneL_Redirect'">JOIN COURSE</a>
    <a class="btn" onclick="location.href='https://t.me/EviLKeRneL'">CONTACT OWNER</a>
  </div>
</header>

<section>
<h2>Pricing Tiers</h2>
<div class="grid">

<div class="card glass">
<h3>FREE</h3>
<p class="price">$0</p>
<ul>
<li>Limited tools</li>
<li>Community access</li>
<li>Basic workflow</li>
</ul>
<button class="btn" onclick="openModal()">GET STARTED</button>
</div>

<div class="card glass">
<h3>PRO</h3>
<p class="price">$49</p>
<ul>
<li>All tools</li>
<li>Full automation</li>
<li>Course access</li>
</ul>
<button class="btn" onclick="location.href='https://t.me/EviLKeRneL_Redirect'">JOIN</button>
</div>

<div class="card glass">
<h3>ELITE</h3>
<p class="price">$99</p>
<ul>
<li>Everything in PRO</li>
<li>Priority updates</li>
<li>Direct support</li>
</ul>
<button class="btn" onclick="location.href='https://t.me/EviLKeRneL'">CONTACT</button>
</div>

</div>
</section>

<footer>
© 2026 EviLKeRneL — Automation beats noise
</footer>

<!-- EMAIL MODAL -->
<div class="modal" id="modal">
  <div class="modal-content glass">
    <h3>Get Updates</h3>
    <input placeholder="Email address">
    <button class="btn" onclick="closeModal()">Submit</button>
  </div>
</div>

<script>
// TERMINAL TYPING
const text = [
  "$ initializing sqlmap automation...",
  "$ loading dork intelligence...",
  "$ tools ready.",
  "$ welcome to EviLKeRneL"
];
let i=0,j=0;
function type(){
  if(i<text.length){
    if(j<text[i].length){
      document.getElementById("typing").innerHTML += text[i][j++];
      setTimeout(type,40);
    }else{
      document.getElementById("typing").innerHTML += "\\n";
      i++; j=0;
      setTimeout(type,400);
    }
  }
}
type();

// MATRIX RAIN
const canvas=document.getElementById("matrix");
const ctx=canvas.getContext("2d");
canvas.width=innerWidth; canvas.height=innerHeight;
const letters="01";
const cols=canvas.width/20;
const drops=Array(Math.floor(cols)).fill(1);
function draw(){
  ctx.fillStyle="rgba(0,0,0,0.05)";
  ctx.fillRect(0,0,canvas.width,canvas.height);
  ctx.fillStyle="#11e87d";
  ctx.font="16px monospace";
  drops.forEach((y,i)=>{
    const text=letters[Math.floor(Math.random()*letters.length)];
    ctx.fillText(text,i*20,y*20);
    if(y*20>canvas.height&&Math.random()>0.975)drops[i]=0;
    drops[i]++;
  });
}
setInterval(draw,50);

// MODAL
function openModal(){document.getElementById("modal").style.display="flex";}
function closeModal(){document.getElementById("modal").style.display="none";}
</script>

</body>
</html>
"""

@app.route("/")
def index():
    return Response(HTML, mimetype="text/html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
