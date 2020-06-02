
/* Initialize the required constants. "Discord" gets the variables, functions and such for the discord.js library, while
client makes a new object from the discord.js library. */
/*
const Discord = require('discord.js');
const client = new Discord.Client();


// Whenever the client is on, the console will log "Logged in as (insert bot name here)" if successfully started and ready.
client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
  if (msg.content === 'ping') {
    msg.reply('Pong!');
  }
});
*/
module.exports = {
  const Discord = require('discord.js');
  const client = new Discord.Client();


  //  Whenever the client is on, the console will log "Logged in as (insert bot name here)" if successfully started and ready.
  client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
  });

  client.on('message', msg => {
    if (msg.content === 'ping') {
      msg.reply('Pong!');
   }
  });
}
