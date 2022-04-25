let sessionClose = document.querySelector(".logout-btn")

if (sessionClose) {
	sessionClose.addEventListener('click', function() {
	window.localStorage.clear()
	})
}
