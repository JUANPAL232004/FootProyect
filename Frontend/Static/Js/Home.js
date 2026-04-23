let isMoving = false;

function moveSlide(direction) {
    if (isMoving) return; // Si ya se está moviendo, ignorar el clic

    const grid = document.getElementById('menuGrid');
    // Obtenemos los items actualizados en cada clic
    const items = grid.querySelectorAll('.menu-item'); 
    
    // Si tienes muy pocos items, no vale la pena mover el carrusel
    const visibleItems = window.innerWidth <= 768 ? 1 : 3;
    if (items.length <= visibleItems) return; 

    isMoving = true;
    
    // Calculamos el ancho de desplazamiento (ancho del item + gap de 20px)
    const itemWidth = items[0].offsetWidth + 20; 

    // --- DIRECCIÓN DERECHA (Siguiente) ---
    if (direction === 1) {
        // 1. Deslizamos hacia la izquierda
        grid.style.transition = 'transform 0.5s ease-in-out';
        grid.style.transform = `translateX(-${itemWidth}px)`;

        // 2. Esperamos a que termine la transición visual (500ms)
        setTimeout(() => {
            grid.style.transition = 'none'; // Apagamos animaciones
            
            // Magia: Movemos el primer elemento físico al final de la lista
            grid.appendChild(grid.firstElementChild); 
            
            // Reseteamos la posición del grid a 0
            grid.style.transform = 'translateX(0)'; 
            isMoving = false;
        }, 500); 
    } 
    // --- DIRECCIÓN IZQUIERDA (Anterior) ---
    else if (direction === -1) {
        // 1. Magia previa: Movemos el último elemento al principio SIN animación
        grid.prepend(grid.lastElementChild);
        grid.style.transition = 'none';
        
        // 2. Ocultamos ese elemento recién movido hacia la izquierda
        grid.style.transform = `translateX(-${itemWidth}px)`;

        // 3. Damos un micro-retraso para que el navegador procese el cambio
        setTimeout(() => {
            // 4. Encendemos la animación y deslizamos a la posición 0
            grid.style.transition = 'transform 0.5s ease-in-out';
            grid.style.transform = 'translateX(0)';
            
            setTimeout(() => {
                isMoving = false;
            }, 500);
        }, 20); // 20ms es suficiente para que el navegador reaccione
    }
}