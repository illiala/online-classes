# metaprogramming to the rescue!

class Numeric
  @@currencies = {'dollar' => 1, 'yen' => 0.013, 'euro' => 1.292, 'rupee' => 0.019}
  def method_missing(method_id)
    singular_currency = method_id.to_s.gsub( /s$/, '')
    if @@currencies.has_key?(singular_currency)
      self * @@currencies[singular_currency]
    else
      super
    end
  end

  def in(to_curr)
    to_curr = to_curr.to_s.gsub( /s$/, '')
    if @@currencies.has_key?(to_curr)
      self / @@currencies[to_curr]
    end
  end
end

# Support the currencies 'dollars', 'euros', 'rupees' , 'yen'
# Both the singular and plural forms of each currency should be acceptable, e.g.
puts "1.dollar.in(:rupees) = #{1.dollar.in(:rupees)}"
puts "10.rupees.in(:euro) = #{10.rupees.in(:euro)}"
puts "5.dollars.in(:euros) = #{5.dollars.in(:euros)}"
puts "10.euros.in(:rupees) = #{10.euros.in(:rupees)}"
