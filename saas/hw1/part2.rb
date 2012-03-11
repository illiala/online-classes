class CartesianProduct
  include Enumerable
  
  attr_accessor :list1
  attr_accessor :list2


  def initialize(list1, list2) 
    @list1 = list1
    @list2 = list2
  end  

  def each
    @list1.each { |el1|
      @list2.each { |el2|
        yield [el1, el2]
      }
    }
  end

end

c = CartesianProduct.new([:a,:b], [4,5])
c.each { |elt| puts elt.inspect }
# [:a, 4]
# [:a, 5]
# [:b, 4]
# [:b, 5]

c = CartesianProduct.new([:a,:b], [])
c.each { |elt| puts elt.inspect }
# (nothing printed since Cartesian product
# of anything with an empty collection is empty)
