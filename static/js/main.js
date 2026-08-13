document.addEventListener('DOMContentLoaded', function () {
    const sidebarToggle = document.getElementById('sidebarToggle');
    const sidebar = document.querySelector('.sidebar');

    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener('click', function (e) {
            e.stopPropagation();
            sidebar.classList.toggle('open');
        });

        document.addEventListener('click', function (e) {
            if (window.innerWidth <= 992) {
                if (!sidebar.contains(e.target) && !sidebarToggle.contains(e.target)) {
                    sidebar.classList.remove('open');
                }
            }
        });
    }

    document.querySelectorAll('.like-btn').forEach(function (btn) {
        btn.addEventListener('click', function () {
            const url = this.dataset.url;
            if (!url) return;

            fetch(url, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Content-Type': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest'
                },
                credentials: 'same-origin'
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    if (data.status === 'liked' || data.status === 'unliked') {
                        const countSpan = this.querySelector('.count');
                        if (countSpan) countSpan.textContent = data.count;

                        if (data.status === 'liked') {
                            this.classList.add('liked');
                        } else {
                            this.classList.remove('liked');
                        }
                    }
                })
                .catch(err => {
                    console.warn('AJAX error:', err);
                });
        });
    });

    document.querySelectorAll('.reply-btn').forEach(function (btn) {
        btn.addEventListener('click', function () {
            const tweetId = this.dataset.tweetId;
            if (tweetId) {
                const replyForm = document.querySelector(`.reply-compose[data-tweet-id="${tweetId}"]`);
                if (replyForm) {
                    replyForm.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    replyForm.querySelector('textarea')?.focus();
                }
            }
        });
    });

    document.querySelectorAll('.share-btn').forEach(function (btn) {
        btn.addEventListener('click', function () {
            const tweet = this.closest('.tweet');
            if (tweet) {
                const tweetId = tweet.dataset.tweetId;
                if (tweetId) {
                    const url = window.location.origin + '/tweet/' + tweetId + '/';
                    if (navigator.clipboard) {
                        navigator.clipboard.writeText(url).then(() => {
                            showToast('لینک کپی شد!');
                        }).catch(() => {
                            prompt('لینک توییت:', url);
                        });
                    } else {
                        prompt('لینک توییت:', url);
                    }
                }
            }
        });
    });

    document.querySelectorAll('.tweet').forEach(function (tweetDiv) {
        tweetDiv.addEventListener('click', function (e) {
            const target = e.target;
            if (target.closest('a') || target.closest('button') || target.closest('.action-btn')) {
                return;
            }
            const detailUrl = this.dataset.detailUrl;
            if (detailUrl) {
                window.location.href = detailUrl;
            }
        });
    });

    document.querySelectorAll('.tweet').forEach(function (tweetDiv) {
        tweetDiv.addEventListener('click', function (e) {
            const target = e.target;
            if (target.closest('a') || target.closest('button') || target.closest('.action-btn')) {
                return;
            }
            const detailUrl = this.dataset.detailUrl;
            if (detailUrl) {
                window.location.href = detailUrl;
            }
        });
    });

    document.querySelectorAll('.reply-context-link, .action-btn.reply-btn').forEach(function (link) {
        link.addEventListener('click', function (e) {
            e.stopPropagation();
        });
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function showToast(message) {
    const toast = document.createElement('div');
    toast.className = 'toast-notification';
    toast.textContent = message;
    toast.style.cssText = `
        position: fixed;
        bottom: 2rem;
        left: 50%;
        transform: translateX(-50%);
        background: var(--bg-card);
        color: var(--text-primary);
        padding: 0.75rem 1.5rem;
        border-radius: var(--radius-full);
        border: 1px solid var(--border-color);
        box-shadow: 0 8px 24px var(--shadow-color);
        font-weight: 500;
        z-index: 9999;
        animation: slideUp 0.3s ease-out;
    `;
    document.body.appendChild(toast);
    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateX(-50%) translateY(20px)';
        toast.style.transition = 'opacity 0.3s, transform 0.3s';
        setTimeout(() => toast.remove(), 400);
    }, 2500);
}

const styleSheet = document.createElement("style");
styleSheet.textContent = `
    @keyframes slideUp {
        from { opacity: 0; transform: translateX(-50%) translateY(20px); }
        to { opacity: 1; transform: translateX(-50%) translateY(0); }
    }
`;
document.head.appendChild(styleSheet);