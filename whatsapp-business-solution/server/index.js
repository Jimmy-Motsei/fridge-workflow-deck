import 'dotenv/config'
import express from 'express'
const app = express()
app.use(express.json())
app.get('/webhook', (req, res) => {
  const mode = req.query['hub.mode']
  const token = req.query['hub.verify_token']
  const challenge = req.query['hub.challenge']
  if (mode === 'subscribe' && token === process.env.VERIFY_TOKEN) return res.status(200).send(challenge)
  return res.sendStatus(403)
})
app.post('/webhook', (req, res) => { console.log('Inbound payload:', JSON.stringify(req.body, null, 2)); res.sendStatus(200) })
app.listen(process.env.PORT || 3000, () => console.log('Webhook listening'))
