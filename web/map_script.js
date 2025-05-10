// map_script.js

document.addEventListener('DOMContentLoaded', function () {
    // 示例：切换图层按钮的交互
    const layerOptions = document.querySelectorAll('.layer-options .layer-option');
    layerOptions.forEach(button => {
        button.addEventListener('click', function() {
            // 移除其他按钮的 active 类
            layerOptions.forEach(btn => btn.classList.remove('active'));
            // 给当前点击的按钮添加 active 类
            this.classList.add('active');
            
            // 在这里可以添加切换图层的逻辑
            console.log('切换到图层:', this.textContent); 
        });
    });

    // 示例：地图控件按钮的交互 (仅打印日志)
    const mapControlButtons = document.querySelectorAll('.map-control-btn');
    mapControlButtons.forEach(button => {
        button.addEventListener('click', function() {
            console.log('点击地图控件:', this.title);
            // 在这里可以添加实际的地图控制逻辑 (如缩放、定位)
        });
    });

    // 如果使用地图库 (例如 Leaflet), 在这里初始化地图:
    /*
    if (typeof L !== 'undefined') { // 检查 Leaflet 是否已加载
        // 初始化地图
        const map = L.map('mapId').setView([30.2741, 120.1551], 13); // 示例坐标：杭州

        // 添加瓦片图层 (例如 OpenStreetMap)
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        // 可以在这里添加标记、图层等
    } else {
        console.warn('地图库 (如 Leaflet) 未加载。请确保已正确引入。');
    }
    */
    console.log('舆情地图页脚本已加载');
});