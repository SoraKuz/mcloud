import axios from 'axios';

const TrackCreatePost = ( label, image, track) => {
  let formData = new FormData();
  formData.append("data", {title: label, "publish_after_creation": true})
  formData.append("poster_file", image.binary)
  formData.append("track_file", track.binary)
  return (
   
    axios.post('https://ichetiva.ru/api/tracks/', 
     formData , 
    {
        headers: 
        {"Authorization": `Bearer ${localStorage.getItem('Token')}`}
    })
      .then(function (response) {
        console.log(response)
        
      })
      .catch(function (error) {
        console.log(error)
        console.log(formData)
      }));
  
/*
  axios.post({
    method: "post",
    url: 'https://ichetiva.ru/api/tracks/',
    data: formData,
    headers: {"Authorization": `Bearer ${localStorage.getItem('Token')}`}
  })
  
  )*/
};

export default TrackCreatePost