document.addEventListener('DOMContentLoaded', () => {
    const menuItems = document.querySelectorAll('.menu li');

    menuItems.forEach(item => {
        item.addEventListener('click', function(event) {
            // 阻止链接的默认行为，如果href是"#"
            if (this.querySelector('a').getAttribute('href') === '#') {
                event.preventDefault();
            }

            // 移除所有菜单项的 active 类
            menuItems.forEach(i => i.classList.remove('active'));
            
            // 给当前点击的菜单项添加 active 类
            this.classList.add('active');

            // 你可以在这里添加更多逻辑，比如根据点击的菜单项加载不同的内容
            const pageName = this.querySelector('a').textContent;
            console.log(`导航到: ${pageName}`);
            // 示例：更新主内容区的标题
            const mainHeader = document.querySelector('.main-header h1');
            if (mainHeader) {
                mainHeader.textContent = pageName;
            }
        });
    });

    // 示例：给按钮添加点击事件监听
    const generateReportButton = document.querySelector('.btn-primary');
    const exportDataButton = document.querySelector('.btn-secondary');

    if (generateReportButton) {
        generateReportButton.addEventListener('click', () => {
            alert('“一键生成简报”功能待实现！');
        });
    }

    if (exportDataButton) {
        exportDataButton.addEventListener('click', () => {
            alert('“导出当前数据”功能待实现！');
        });
    }

    console.log('iSight 脚本已加载并执行完毕。');
});