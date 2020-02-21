export default function postbudge(budge) {
  return axios.post('/v1/budget/', budge).then(res => {
    return res.data;
  });
}
