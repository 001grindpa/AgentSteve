document.addEventListener('DOMContentLoaded', () => {
    if (document.body.id === "index") {
        const hi = document.querySelector(".hi");
        const ready = hi.querySelectorAll(".ready");
        const cl = hi.querySelector("#cl");
        const loader = document.querySelector(".loader");
        const index = document.querySelector(".index");
        const cleanForm = document.querySelector("#cleanForm");
        const ingre = document.querySelector(".ingredients");
        const qCont = document.querySelector(".query");
        const q2Cont = document.querySelector(".query2");

        cleanForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            // qCont.style.display = "none";
            // q2Cont.style.display = "block";
            let form = new FormData(cleanForm);
            let query = form.get("q");

            let r = await fetch("/clean", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({q: query})
            });
            let data = await r.json();
            console.log(data);
            ingre.textContent = JSON.stringify(data.msg);
        })

        window.addEventListener("load", () => {
            loader.style.display = "none";
            index.style.display = "block";
        });

        if (cl.value === "cancel") {
            hi.style.display = "none";
        }

        for (let i=0; i < ready.length; i++) {
            ready[i].addEventListener("click", async () => {
                hi.style.display = "none";

                let r = await fetch("/", {
                    method: "post",
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify({q: "cancel"})
                });
                let data = await r.json();
                console.log(data, cl.value);
            });
        };
    }
});