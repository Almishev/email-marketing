
					  const segments = ["Подарък 1", "Подарък 2", "Подарък 3", "Подарък 4", "Подарък 5", "Опитай пак"];
					  const colors = ["#ffcc00", "#ff9900", "#ff6600", "#ff3300", "#ff0033", "#cc00ff"];
					  const canvas = document.getElementById("wheelCanvas");
					  const ctx = canvas.getContext("2d");
					  const spinButton = document.getElementById("spinButton");
					  const resultDisplay = document.getElementById("result");
				  
					  let startAngle = 0;
					  let spinning = false;
					  let speed = 0; // Начална скорост
					  let deceleration = 0; // Намаляване на скоростта
				  
					  // Рисуване на колелото
					  function drawWheel() {
						const radius = canvas.width / 2;
						const arcSize = (2 * Math.PI) / segments.length;
				  
						for (let i = 0; i < segments.length; i++) {
						  ctx.beginPath();
						  ctx.fillStyle = colors[i];
						  ctx.moveTo(radius, radius);
						  ctx.arc(radius, radius, radius, startAngle + i * arcSize, startAngle + (i + 1) * arcSize);
						  ctx.fill();
						  ctx.save();
						  ctx.translate(radius, radius);
						  ctx.rotate(startAngle + (i + 0.5) * arcSize);
						  ctx.fillStyle = "#fff";
						  ctx.textAlign = "center";
						  ctx.font = "bold 14px sans-serif";
						  ctx.fillText(segments[i], radius / 2, 5);
						  ctx.restore();
						}
					  }
				  
					  // Анимация за завъртане
					  function animate() {
						if (speed > 0) {
						  startAngle += speed; // Увеличаваме ъгъла според скоростта
						  speed -= deceleration; // Постепенно намаляване на скоростта
						  if (speed < 0) speed = 0; // Уверяваме се, че скоростта не става отрицателна
						  ctx.clearRect(0, 0, canvas.width, canvas.height);
						  drawWheel();
						  requestAnimationFrame(animate);
						} else {
						  spinning = false;
				  
						  // Изчисляване на резултата
						  const segmentAngle = (2 * Math.PI) / segments.length;
						  const winningSegmentIndex = Math.floor(((startAngle + Math.PI / 2) % (2 * Math.PI)) / segmentAngle);
						  const winningSegment = segments[segments.length - 1 - winningSegmentIndex];
				  
						  // Показваме резултата с промокода
						  if (winningSegment === "Подарък 1" || winningSegment === "Подарък 3") {
							resultDisplay.textContent = "Печелиш промокод за 10% отстъпка: K9UY";
						  } else if (winningSegment === "Подарък 2" || winningSegment === "Подарък 4") {
							resultDisplay.textContent = "Печелиш промокод за безплатна доставка: P@RT";
						  } else {
							resultDisplay.textContent = "Опитай пак!";
						  }
				  
						  // Скриваме бутона след завъртането
						  spinButton.style.display = "none";
						}
					  }
				  
					  function spinWheel() {
						if (spinning) return;
						spinning = true;
				  
						spinButton.style.display = "none"; // Скриваме бутона
				  
						speed = Math.random() * 0.1 + 0.3; // Начална скорост (случайна)
						deceleration = speed / 150; // По-бавно намаляване на скоростта
						animate(); // Стартираме анимацията
					  }
				  
					  spinButton.addEventListener("click", spinWheel);
					  drawWheel();
				