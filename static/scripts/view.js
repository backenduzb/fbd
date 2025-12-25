const menuBtn = document.getElementById('menu-btn');
        menuBtn.onclick = () => {
            document.body.classList.toggle('sidebar-open');
        };

        const othersBtn = document.getElementById('other-btn');
        othersBtn.onclick = () => {
            document.body.classList.remove('save-as-open');
            document.body.classList.toggle('others-open');
        };

        const saveAsBtn = document.getElementById('save-as-btn');
        if (saveAsBtn) {
            saveAsBtn.onclick = () => {
                document.body.classList.remove('others-open');
                document.body.classList.toggle('save-as-open');
            };
        }

        const closeSaveBtn = document.getElementById('close-save-btn');
        if (closeSaveBtn) {
            closeSaveBtn.onclick = () => {
                document.body.classList.remove('save-as-open');
            };
        }

        const fsBtn = document.getElementById('fullscreen-btn');
        fsBtn.onclick = () => {
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen().catch((err) => {
                    alert(`Fullscreen rejimga o'tilmadi: ${err.message}`);
                });
            } else {
                document.exitFullscreen();
            }
        };

        const img = document.getElementById('pdf-img');
        let scale = 1;
        let rotation = 0;
        let translateX = 0;
        let translateY = 0;
        let isDragging = false;
        let startX = 0;
        let startY = 0;
        let rafId = null;

        function applyTransform() {
            img.style.transform = `translate3d(${translateX}px, ${translateY}px, 0) scale(${scale}) rotate(${rotation}deg)`;
            rafId = null;
        }

        function requestUpdate() {
            if (rafId) return;
            rafId = requestAnimationFrame(applyTransform);
        }

        document.getElementById('zoom-in').onclick = () => {
            scale += 0.1;
            requestUpdate();
        };

        document.getElementById('zoom-out').onclick = () => {
            scale = Math.max(0.1, scale - 0.1);
            requestUpdate();
        };

        document.getElementById('rotate-cw').onclick = () => {
            rotation += 90;
            requestUpdate();
        };

        document.getElementById('rotate-ccw').onclick = () => {
            rotation -= 90;
            requestUpdate();
        };

        img.addEventListener('dragstart', e => e.preventDefault());

        img.addEventListener('mousedown', (e) => {
            isDragging = true;
            startX = e.clientX - translateX;
            startY = e.clientY - translateY;
            img.style.cursor = 'grabbing';
        });

        document.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            translateX = e.clientX - startX;
            translateY = e.clientY - startY;
            requestUpdate();
        });

        document.addEventListener('mouseup', () => {
            isDragging = false;
            img.style.cursor = 'grab';
        });

document.getElementById('save-file-btn').onclick = async () => {
    const nameInput = document.querySelector('.text-input');
            const type = document.getElementById('file-select').value;

            let fileName = nameInput.value.trim();
            if (!fileName) {
                alert("Имя файла не указано");
            return;
    }

            let fileUrl = "";
            let ext = "";

            if (type === "pdf") {
                fileUrl = "{{ doc.file.url }}";
            ext = ".pdf";
    } else if (type === "jpg") {
                fileUrl = "{{ pdf_preview }}";
            ext = ".jpg";
    }

            try {
        const response = await fetch(fileUrl);
            const blob = await response.blob();

            const blobUrl = URL.createObjectURL(blob);

            const a = document.createElement("a");
            a.href = blobUrl;
            a.download = fileName + ext;

            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);

            URL.revokeObjectURL(blobUrl);
    } catch (e) {
                alert("Faylni yuklab bo‘lmadi");
            console.error(e);
    }
};