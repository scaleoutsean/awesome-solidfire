#!/usr/bin/env perl

# Simple Perl 5 script that lists SolidFire (tenant/storage) accounts.
# Tested with SolidFire 12.5. Enable TLS validation for production use.
# 
# $ ./try.pl 
# 
# Account: sean (ID: 1)
#  Status: active
#   Volumes: 10, 11, 13, 15, 97
# 
# Author: @scaleoutSean (github.com/scaleoutsean/)
# License: Apache License 2.0
# 


use strict;
use warnings;
use LWP::UserAgent;
use HTTP::Request;
use JSON::XS;

my $sf_url = 'https://192.168.1.34/json-rpc/12.5/';
my $user = 'admin';
my $pass = 'xxxxx';

# Prepare JSON-RPC request
my $request_data = {
    method => "ListAccounts",
    params => { includeStorageContainers => JSON::XS::false },
    id     => 1,
};
my $json = encode_json($request_data);

# Set up HTTP POST
my $ua = LWP::UserAgent->new(ssl_opts => { verify_hostname => 0 });
my $req = HTTP::Request->new(POST => $sf_url);
$req->authorization_basic($user, $pass);
$req->header('Content-Type' => 'application/json');
$req->content($json);

# Send request
my $resp = $ua->request($req);
die "HTTP error: " . $resp->status_line unless $resp->is_success;

# Parse response
my $resp_data = decode_json($resp->decoded_content);

# Extract accounts
my $accounts = $resp_data->{result}{accounts};
foreach my $acct (@$accounts) {
    print "Account: $acct->{username} (ID: $acct->{accountID})\n";
    print "  Status: $acct->{status}\n";
    print "  Volumes: " . join(", ", @{$acct->{volumes}}) . "\n";
}
