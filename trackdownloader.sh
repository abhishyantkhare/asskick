#!/bin/bash
i=0
url1="https://api.spotify.com/v1/users/127597966/playlists/3n3qsDmXCfXWj0ONPUOqhf/tracks?limit=100&offset="

until [ $i -gt 2700 ] 
do
	num=$i
	url=$url1$num
	json=$(curl -X GET $url -H "Accept: application/json" -H "Authorization: Bearer BQAoUAHFSLwER7_Gy4TooHoGWzS2BjuyspU4cfY773rmvLvQSKidnkm_JeVlIlztdDsEHBygNcG6zdZcptst9usf1L9qUaQL2tXmO9JMUjBS997rzHpg6VTpG2WEeI_xZq5DPy5QIJA0LA")
	echo $json>>/run/media/abhishyant/Storage/Python/music_torrent_scripts/asskick/tracks.json
	i=$((i+100))
done