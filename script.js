document.getElementById('adminBtn').addEventListener('click', () => {
    document.getElementById('adminSection').classList.remove('hidden');
    document.getElementById('adminSection').classList.add('visible');
    document.getElementById('siteviewSection').classList.remove('visible');
    document.getElementById('siteviewSection').classList.add('hidden');
});

document.getElementById('siteviewBtn').addEventListener('click', () => {
    document.getElementById('siteviewSection').classList.remove('hidden');
    document.getElementById('siteviewSection').classList.add('visible');
    document.getElementById('adminSection').classList.remove('visible');
    document.getElementById('adminSection').classList.add('hidden');
});
