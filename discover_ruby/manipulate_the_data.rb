#!/usr/bin/ruby

require 'httpclient'
require 'json'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token e107aed5a9acf8df3246ffc645de998ef2046d5a'
}

http = HTTPClient.new
response = http.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc')

ruby_projects = JSON.parse(response)
puts ruby_projects["items"].map {|index| index["full_name"]}
