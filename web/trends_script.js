// trends_script.js
document.addEventListener('DOMContentLoaded', function () {
    console.log('情感趋势页脚本已加载');

    const chartCanvas = document.getElementById('sentimentTrendChart');
    const fallbackText = document.getElementById('chartFallbackText');

    // if (chartCanvas && typeof Chart !== 'undefined') { // 检查 Chart.js 是否已加载
        // 示例图表数据 (与图片中的柱状图类似)
        // const data = {
        //     labels: ['12:00', '13:00', '14:00', '15:00', '16:00'],
        //     datasets: [
        //         {
        //             label: '高兴',
        //             data: [2200, 1200, 4500, 4800, 2900], // 示例数据
        //             backgroundColor: '#5470c6', // 蓝色
        //             borderColor: '#5470c6',
        //             borderWidth: 1
        //         },
        //         {
        //             label: '生气',
        //             data: [2400, 800, 3900, 4800, 1800], // 示例数据
        //             backgroundColor: '#91cc75', // 紫色 (根据图片调整，这里用绿色代替)
        //             borderColor: '#91cc75',
        //             borderWidth: 1
        //         },
        //         {
        //             label: '平和',
        //             data: [1000, 300, 200, 3600, 2500], // 示例数据
        //             backgroundColor: '#fac858', // 绿色 (根据图片调整，这里用黄色代替)
        //             borderColor: '#fac858',
        //             borderWidth: 1
        //         }
        //     ]
        // };

        // 图表配置
        // const config = {
        //     type: 'bar',
        //     data: data,
        //     options: {
        //         responsive: true,
        //         maintainAspectRatio: false,
        //         scales: {
        //             y: {
        //                 beginAtZero: true,
        //                 ticks: {
        //                     // 根据图片调整y轴刻度
        //                     stepSize: 960,
        //                     callback: function(value) {
        //                         return value;
        //                     }
        //                 }
        //             },
        //             x: {
        //                 grid: {
        //                     display: false // 不显示x轴网格线
        //                 }
        //             }
        //         },
        //         plugins: {
        //             legend: {
        //                 display: false // 我们在HTML中自定义了图例
        //             },
        //             title: {
        //                 display: false // 我们在HTML中自定义了标题
        //             }
        //         }
        //     }
        // };

        // 创建图表
        // new Chart(chartCanvas, config);
    // } else {
    //     if(fallbackText) fallbackText.style.display = 'block';
    //     console.warn('Chart.js 未加载或 Canvas 元素未找到。请确保已正确引入 Chart.js 并在 HTML 中有 ID 为 "sentimentTrendChart" 的 canvas 元素。');
    // }

    // 时间粒度选择器的交互 (可选)
    const timeSelector = document.getElementById('timeGranularitySelector');
    if (timeSelector) {
        timeSelector.addEventListener('change', function() {
            console.log('选择的时间粒度:', this.value);
            // 在此可以添加根据选择重新加载或更新图表数据的逻辑
        });
    }
});