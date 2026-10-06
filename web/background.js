var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
var bgg = document.getElementById("bg_glow");
w = ctx.canvas.width = window.innerWidth;
h = ctx.canvas.height = window.innerHeight;
window.onresize = function() {
    w = ctx.canvas.width = window.innerWidth;
    h = ctx.canvas.height = window.innerHeight;
    maxHeight = h * .9;
    minHeight = h * .5;
    dots = [];
    pushDots();
    ctx.globalCompositeOperation = "source-over";
};
dots = [{}];
mx = 0; my = 0;
md = 100;
maxWidth = 15;
minWidth = 2;
maxHeight = h * .9;
minHeight = h * .5;
maxSpeed = 35;
minSpeed = 6;
hue = 231;       /* Latte lavender hue */
hueDif = 30;
glow = 8;
/* Use "source-over" instead of "lighter" so light colors don't blow out */
ctx.globalCompositeOperation = "source-over";

function pushDots() {
    for (i = 1; i < md; i++) {
        dots.push({
            x: Math.random() * w,
            y: Math.random() * h / 2,
            h: Math.random() * (maxHeight - minHeight) + minHeight,
            w: Math.random() * (maxWidth - minWidth) + minWidth,
            c: Math.random() * ((hue + hueDif) - (hue - hueDif)) + (hue - hueDif),
            m: Math.random() * (maxSpeed - minSpeed) + minSpeed
        });
    }
} pushDots();

function render() {
    ctx.clearRect(0, 0, w, h);
    for (i = 1; i < dots.length; i++) {
        ctx.beginPath();
        grd = ctx.createLinearGradient(dots[i].x, dots[i].y, dots[i].x + dots[i].w, dots[i].y + dots[i].h);
        grd.addColorStop(.0,  "hsla(" + dots[i].c + ",60%,72%,.0)");
        grd.addColorStop(.2,  "hsla(" + (dots[i].c + 10) + ",65%,68%,.35)");
        grd.addColorStop(.5,  "hsla(" + (dots[i].c + 20) + ",70%,65%,.55)");
        grd.addColorStop(.8,  "hsla(" + (dots[i].c + 30) + ",60%,68%,.35)");
        grd.addColorStop(1.,  "hsla(" + (dots[i].c + 50) + ",55%,72%,.0)");
        ctx.shadowBlur = glow;
        ctx.shadowColor = "hsla(" + dots[i].c + ",60%,70%,0.5)";
        ctx.fillStyle = grd;
        ctx.fillRect(dots[i].x, dots[i].y, dots[i].w, dots[i].h);
        ctx.closePath();
        dots[i].x += dots[i].m / 100;
        if (dots[i].x > w + maxWidth) {
            dots[i].x = -maxWidth;
        }
    }
    window.requestAnimationFrame(render);
}

/* Latte-style soft lavender radial glow */
bgg.style.background = "radial-gradient(ellipse at center, hsla(" + hue + ",55%,75%,0.55) 0%, rgba(239,241,245,0) 70%)";
render();
