import streamlit as st
import streamlit.components.v1 as com




com.html("""
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>Ayurvedic Herbs</title>
    <style>
        body {
            background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
            background-size: cover;
            background-repeat:no-repeat
            color: #333;
            font-family: Arial, sans-serif;
            font-size: 18px;
            line-height: 1.5;
            margin: 0;
            padding: 0;
            height: auto;
            width: auto;
        }

        h1,
        h2 {
            margin: 0;
            text-align: center;
        }

        h1 {
            font-size: 3rem;
            margin-top: 2rem;
            text-shadow: 2px 2px #fff;
        }

        h2 {
            font-size: 2rem;
            margin-bottom: 1rem;
            text-shadow: 1px 1px #fff;
        }

        img {
            display: block;
            margin: 0 auto;
            max-width: 100%;
        }

        p {
            margin-bottom: 1.5rem;
            text-align: justify;
        }

        .btn {
            background-color: #4CAF50;
            border: none;
            border-radius: 4px;
            color: white;
            cursor: pointer;
            display: inline-block;
            font-size: 1.2rem;
            margin: 2rem auto;
            padding: 1rem 2rem;
            text-align: center;
            text-decoration: none;
            transition-duration: 0.4s;
        }

        .btn:hover {
            background-color: #3e8e41;
            color: #fff;
            transition-duration: 0.4s;
        }
    </style>
</head>

<body>
    <main>
        <h1>Ayurvedic Herbs for Body Wellness</h1>

        <section>
            <h2>Turmeric</h2>
            <img src="https://www.istockphoto.com/photo/aswagandha-root-and-powder-isolated-on-white-background-gm1333961124-416268491?utm_source=unsplash&utm_medium=affiliate&utm_campaign=srp_photos_top&utm_content=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Fashwagandha&utm_term=ashwagandha%3A%3A%3A" alt="Turmeric">
            <p>Turmeric is a spice that has been used in Ayurvedic medicine for thousands of years. It contains a
                powerful antioxidant called curcumin, which has anti-inflammatory properties. Turmeric is used to treat
                a variety of conditions such as arthritis, indigestion, and skin problems. Turmeric is available in
                various forms such as capsules, powders, and teas.</p>
        </section>

        <section>
            <h2>Neem</h2>
            <img src="https://cdn.pixabay.com/photo/2016/10/22/17/46/neem-leaves-1764276_960_720.jpg" alt="Neem">
            <p>Neem is a tree whose leaves, bark, and seeds have been used in Ayurvedic medicine for centuries. It is
                known for its anti-inflammatory, anti-bacterial, and anti-fungal properties. Neem is used to treat a
                variety of conditions such as acne, eczema, and dandruff. Neem is available in various forms such as
                capsules, powders, and oils.</p>
        </section>

        <section>
            <h2>Ashwagandha</h2>
            <img src="https://cdn.pixabay.com/photo/2017/02/15/08/52/ashwagandha-2064338_960_720.jpg" alt="Ashwagandha">
            <p>Ashwagandha is an herb that has been used in Ayurvedic medicine for over 3,000 years. It is known for its
                ability to reduce stress and anxiety, improve brain function, and boost fertility. Ashwagandha is
                available in various forms such as capsules, powders, and teas.</p>
        </section>

        <section>
            <h2>Brahmi</h2>
            <img src="https://cdn.pixabay.com/photo/2017/02/15/08/50/brahmi-2064334_960_720.jpg" alt="Brahmi">
            <p>Brahmi is a herb that has been used in Ayurvedic medicine for centuries. It is known for its ability to
                improve memory, reduce anxiety and stress, and promote overall brain health. Brahmi is available in
                various forms such as capsules, powders, and teas.</p>
        </section>

        <a href="https://www.webmd.com/balance/guide/ayurvedic-treatments" class="btn" target="_blank">Learn more about
            Ayurvedic treatments</a>
    </main>
</body>

</html>

""", width=1300,height=1800, scrolling=True
         )
