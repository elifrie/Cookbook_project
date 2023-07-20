import {useState, useEffect} from 'react'

const Slideshow = ({ images }) => {
    const [currentSlide, setCurrentSlide] = useState(0);
    let [display, setDisplay] = useState(true)

    function handleSwitch() {
        setDisplay((display) = !display)
    }

    useEffect(() => {
        const interval = setInterval(() => {
            setCurrentSlide((prevSlide) => (prevSlide +1) % images.length);
        }, 3500);

    return () => clearInterval(interval);
}, [images]);

    return (
        <div className = 'slideshow'>
            <img alt = {`Slide ${currentSlide + 1}`} onClick = {handleSwitch} className = 'about-image' src={display ? "../images/about.jpg" : images[currentSlide]}/>
            {/* // <img src = {images[currentSlide]} alt = {`Slide ${currentSlide + 1}`}/> } */}
        </div>
    )
}

export default Slideshow;