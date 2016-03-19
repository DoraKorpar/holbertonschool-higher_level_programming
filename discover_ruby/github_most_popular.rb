#!/usr/bin/ruby

require 'httpclient'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token e107aed5a9acf8df3246ffc645de998ef2046d5a'
}

http = HTTPClient.new
response = http.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc')
puts response
