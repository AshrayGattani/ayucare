import streamlit as st
import streamlit.components.v1 as com

com.html("""
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Ayurvedic Herbs for Body Wellness</title>
	<style>
		body {
			font-family: Arial, sans-serif;
			background-image: url('background.jpg');
			background-repeat: repeat;
		}

		header {
			background-color: #ffffff;
			padding: 20px;
		}

		h1 {
			font-size: 36px;
			color: #4d4d4d;
			text-align: center;
			margin: 0;
		}

		main {
			background-color: #f4f4f4;
			padding: 50px;
		}

		p {
			font-size: 20px;
			line-height: 1.5;
			color: #4d4d4d;
			margin-bottom: 30px;
			text-align: justify;
		}

		ul {
			list-style-type: none;
			margin: 0;
			padding: 0;
		}

		li {
			font-size: 20px;
			color: #4d4d4d;
			margin: 20px 0;
			padding-left: 50px;
			background-repeat: no-repeat;
			background-position: left center;
			line-height: 1.5;
		}

		.ashwagandha {
			background-image:"https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
		}

		.turmeric {
			background-image: url('turmeric.jpg');
		}

		.brahmi {
			background-image: url('brahmi.jpg');
		}

		.ginger {
			background-image: url('ginger.jpg');
		}

		.tulsi {
			background-image: url('tulsi.jpg');
		}

		.triphala {
			background-image: url('triphala.jpg');
		}

		.btn {
			display: inline-block;
			background-color: #4d4d4d;
			color: #fff;
			padding: 10px 20px;
			border-radius: 5px;
			text-decoration: none;
			margin-top: 50px;
		}

		.btn:hover {
			background-color: #333;
		}
	</style>
</head>
<body>
	<header>
		<h1>Ayurvedic Herbs for Body Wellness</h1>
	</header>
	
	<main>
		<section>
			<p>Ayurveda is a traditional Indian system of medicine that focuses on holistic healing of the body, mind, and spirit. Ayurvedic herbs are an important part of this system and are used to treat a variety of ailments and promote overall wellness. Here are some of the most popular Ayurvedic herbs:</p>

			<ul>
				<li class="ashwagandha">Ashwagandha - used to reduce stress and anxiety</li>
				<li class="turmeric">Turmeric - used to reduce inflammation and boost immunity</li>
				<li class="brahmi">Brahmi - used to improve cognitive function and memory</li>
				<li class="ginger">Ginger - used to aid digestion and relieve nausea</li>
				<li class="tulsi">Tulsi - used to boost immunity and reduce stress</li>
				<li class="triphala">Triphala - used as a digestive tonic and detoxifier</li>
			</ul>
			<section>
			<h2>Ashwagandha</h2>
			<img src="ashwagandha.jpg" alt="Ashwagandha">
			<p>Ashwagandha is an adaptogenic herb that has been used for centuries to promote vitality and longevity. It is known to reduce stress and anxiety, improve brain function, and boost immunity. Ashwagandha is available in various forms such as capsules, powders, and teas.</p>
            </section>

            <section>
                <h2>Turmeric</h2>
                <img src="turmeric.jpg" alt="Turmeric">
                <p>Turmeric is a spice that contains curcumin, a potent anti-inflammatory compound. It is used to reduce inflammation in the body, improve brain function, and boost immunity. Turmeric is commonly used in cooking and is also available in the form of capsules and powders.</p>
            </section>

            <section>
                <h2>Brahmi</h2>
                <img src="brahmi.jpg" alt="Brahmi">
                <p>Brahmi is a herb that has been used in Ayurvedic medicine to improve cognitive function and memory. It is also known to reduce anxiety and stress, and promote relaxation. Brahmi is available in various forms such as capsules, powders, and teas.</p>
            </section>

            <section>
                <h2>Ginger</h2>
                <img src="ginger.jpg" alt="Ginger">
                <p>Ginger is a popular spice that is used in cooking as well as in traditional medicine. It is known to aid digestion, relieve nausea and reduce inflammation in the body. Ginger is available fresh, dried, or in the form of capsules and teas.</p>
            </section>

            <section>
                <h2>Tulsi</h2>
                <img src="tulsi.jpg" alt="Tulsi">
                <p>Tulsi, also known as holy basil, is a herb that is considered sacred in India. It is used to boost immunity, reduce stress and anxiety, and improve respiratory health. Tulsi is available fresh, dried, or in the form of teas and capsules.</p>
            </section>

            <section>
                <h2>Triphala</h2>
                <img src="triphala.jpg" alt="Triphala">
                <p>Triphala is a blend of three fruits: amla, haritaki, and bibhitaki. It is used as a digestive tonic and detoxifier in Ayurvedic medicine. Triphala is also known to boost immunity and promote overall wellness. Triphala is available in the form of capsules and powders.</p>
            </section>

            <a href="#" class="btn">Shop Ayurvedic Herbs</a>
        </main>
    </body>
    </html>
""",height=1800,scrolling=True
        
)